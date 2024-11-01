import random,subprocess,sys,os,json,tempfile
from pathlib import Path
from .common import validate_case
from .drift import ks_statistic,threshold
from .quality import accuracy,valid_rows
from .registry import Registry
FAMILIES=('stable','mean-shift','variance-shift','missing','label-flip','small-batch')
def run_case(case):
    validate_case(case)
    if case['family'] not in FAMILIES:raise ValueError('unknown MLOps family')
    n=case['size'];rng=random.Random(case['seed']);reference=[rng.gauss(0,1) for _ in range(128)];rows=[];family=case['family']
    for i in range(n):
        x=rng.gauss(2 if family=='mean-shift' else 0,3 if family=='variance-shift' else 1);y=int(x>=0)
        if family=='label-flip':y=1-y
        if family=='missing' and i%3==0:x=None
        rows.append((x,y))
    clean=valid_rows(rows);missing=n-len(clean);baseline={'weight':1,'bias':0};enough=len(clean)>=16
    d=ks_statistic(reference,[x for x,y in clean]) if clean else 0.;limit=threshold(len(reference),len(clean)) if clean else 1.
    old=accuracy(baseline,clean) if clean else 0.;drift=d>limit;quality_failure=missing/n>.1 or old<.8
    triggered=enough and (drift or quality_failure) and missing/n<=.2 and family!='small-batch'
    promoted=False;newscore=old;job=False
    if triggered:
        split=max(8,len(clean)*2//3);training=clean[:split];holdout=clean[split:]
        env=dict(os.environ);env['PYTHONPATH']=str(Path(__file__).resolve().parents[1]);env['PYTHONDONTWRITEBYTECODE']='1'
        result=subprocess.run([sys.executable,'-m','syslab.retrain'],input=json.dumps({'rows':training}),capture_output=True,text=True,env=env,timeout=10,check=True)
        candidate=json.loads(result.stdout);job=True;newscore=accuracy(candidate,holdout);old_holdout=accuracy(baseline,holdout)
        with tempfile.TemporaryDirectory() as tmp:
            reg=Registry(Path(tmp)/'model.json');promoted=reg.promote(candidate,newscore,old_holdout)
            if promoted:reg.load()
    return {'metrics':{'received':n,'clean':len(clean),'missing':missing,'accounted':len(clean)+missing==n,'ks_statistic':round(d,6),'drift_detected':drift,'quality_failure':quality_failure,'retraining_triggered':triggered,'isolated_job':job,'promoted':promoted,'candidate_accuracy':newscore,'baseline_accuracy':old,'promotion_safe':not promoted or newscore>=.7},'output':{'threshold_approximate':limit,'minimum_clean_samples':16,'execution':'local subprocess, no cloud job'}}
