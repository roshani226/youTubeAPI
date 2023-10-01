import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

def text_test(text,model_data):

    if "Issue" in text.split():
        Issue=1
    else:
        Issue=0

    if "results" in text.split():
        results=1
    else:
        results=0

    if "error" in text.split():
        error=1
    else:
        error=0

    if "outdated" in text.split():
        outdated=1
        print("kk")
    else:
        outdated=0
        print("bb")

    if "wrong" in text.split():
        wrong=1
    else:
        wrong=0

    if "content" in text.split():
        content=1
    else:
        content=0

    if "output" in text.split():
        output=1
    else:
        output=0

    if "difficult" in text.split():
        difficult=1
    else:
        difficult=0

    if "wasting" in text.split():
        wasting=1
    else:
        wasting=0

    if "time" in text.split():
        time=1
    else:
        time=0

    if "doubt" in text.split():
        doubt=1
    else:
        doubt=0

    if "unclear" in text.split():
        unclear=1
    else:
        unclear=0

    if "useless" in text.split():
        useless=1
    else:
        useless=0

    if "incomplete" in text.split():
        incomplete=1
    else:
        incomplete=0

    if "missing" in text.split():
        missing=1
    else:
        missing=0

    if "disagree" in text.split():
        disagree=1
    else:
        disagree=0

    if "quality" in text.split():
        quality=1
    else:
        quality=0

    if "unexpected" in text.split():
        unexpected=1
    else:
        unexpected=0

    if "title" in text.split():
        title=1
    else:
        title=0

    if "less" in text.split():
        less=1
    else:
        less=0

    if "important" in text.split():
        important=1
    else:
        important=0

    if "irrelevant" in text.split():
        irrelevant=1
    else:
        irrelevant=0

    if "problem" in text.split():
        problem=1
    else:
        problem=0

    if "mismatch" in text.split():
        mismatch=1
    else:
        mismatch=0

    if "source" in text.split():
        source=1
    else:
        source=0

    if "code" in text.split():
        code=1
    else:
        code=0

    if "understand" in text.split():
        understand=1
    else:
        understand=0

    if "Type" in text.split():
        Type=1
    else:
        Type=0

    # print(model_data.predict([[Issue,results,error,outdated,wrong,content,output,difficult,wasting,time,doubt,unclear,useless,incomplete,missing,disagree,quality,unexpected,wasting,title,less,irrelevant,problem,mismatch,source,understand,Type]]))
    return (model_data.predict([[Issue,results,error,outdated,wrong,content,output,difficult,wasting,time,doubt,unclear,useless,incomplete,missing,disagree,quality,unexpected,wasting,title,less,irrelevant,problem,mismatch,source,understand,Type]]))