def diffDate(x):
    import datetime
    skrg = datetime.datetime.now()
    from datetime import datetime
    tngglAcak = datetime.strptime(x,"%Y-%m-%d")
    rumus = skrg - tngglAcak
    print(abs(rumus.days))

diffDate("2021-01-01")


