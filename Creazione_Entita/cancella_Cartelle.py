import os, shutil
Dir = os.getcwd()
Dir += "\\Da_Aggiungere"
dom = Dir+"\\domain"
efc = Dir+"\\EntityFrameworkCore"
dom_sha = Dir+"\\domain.shared"
app = Dir+"\\application"
app_con = Dir+"\\application.contracts"
FE = Dir+"\\Front_End"
scelta = input("sicuro di voler eliminare le cartelle?(y/n): ")
if scelta == "y":
    if os.path.exists(app):
        shutil.rmtree(app, ignore_errors=True)
    if os.path.exists(app_con):
        shutil.rmtree(app_con, ignore_errors=True)
    if os.path.exists(dom):
        shutil.rmtree(dom, ignore_errors=True)
    if os.path.exists(dom_sha):
        shutil.rmtree(dom_sha, ignore_errors=True)
    if os.path.exists(efc):
        shutil.rmtree(efc, ignore_errors=True)
    if os.path.exists(FE):
        shutil.rmtree(FE, ignore_errors=True)
else:
    print("ok non le cancellerò")