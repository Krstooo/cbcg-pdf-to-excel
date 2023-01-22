import tabula
import pandas as pd
from time import sleep

# Unesi period u formatu npr  0622
period = '0922'

# 1 - BS
# 2 - BU


#Ovo sve moze pametnije. Znam. Drugi put.


Ckbs = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/ckb/{period}ckb_bs.pdf'
Ckbu = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/ckb/{period}ckb_bu.pdf'

Hipotekarnas = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/hip/{period}hip_bs.pdf'
Hipotekarnau = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/hip/{period}hip_bu.pdf'

Prvas = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/nik/{period}prv_bs.pdf'
Prvau = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/nik/{period}prv_bu.pdf'

Erstes = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/opp/{period}ers_bs.pdf'
Ersteu = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/opp/{period}ers_bu.pdf'

Nlbs = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/mnb/{period}nlb_bs.pdf'
Nlbu = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/mnb/{period}nlb_bu.pdf'

Addikos = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/hyp/{period}adk_bs.pdf'
Addikou = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/hyp/{period}adk_bu.pdf'


Universals = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/ffb/{period}ucb_bs.pdf'
Universalu = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/ffb/{period}ucb_bu.pdf'

Lovcens = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/lov/{period}lov_bs.pdf'
Lovcenu = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/lov/{period}lov_bu.pdf'

Zapads = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/zap/{period}zap_bs.pdf'
Zapadu = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/zap/{period}zap_bu.pdf'

Ziraats = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/zir/{period}zir_bs.pdf'
Ziraatu = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/zir/{period}zir_bu.pdf'

Adriatics = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bs/azm/{period}adr_bs.pdf'
Adriaticu = f'https://www.cbcg.me/slike_i_fajlovi/fajlovi/fajlovi_kontrola_banaka/pokazatelji/banke/bu/azm/{period}adr_bu.pdf'


nazivi1 = [
            Ckbs,
            Ckbu,
            Hipotekarnas,
            Hipotekarnau,
            Prvas,
            Prvau,
            Erstes,
            Ersteu,
            Nlbs,
            Nlbu,
            Zapads,
            Zapadu,
            Ziraats,
            Ziraatu,
            Addikou,
            Universalu,
            Lovcenu,
            Adriaticu
        ]



nazivi2 = [

            Addikos,
            Universals,
            Lovcens,
            Adriatics
        ]




for i in nazivi1:
    df = tabula.read_pdf(i, pages = 'all')[0]
    sheet_name = f'{i[-10:-4]}'
    with pd.ExcelWriter('Bilansi banaka.xlsx', engine='openpyxl', mode = 'a') as writer:  
        df.to_excel(writer, sheet_name= sheet_name)


for i in nazivi2:
    df = tabula.read_pdf(i, pages = 'all')[1]   #.iloc[:,-1]
    sheet_name = f'{i[-10:-4]}'
    with pd.ExcelWriter('Bilansi banaka.xlsx', engine='openpyxl', mode = 'a') as writer:  
        df.to_excel(writer, sheet_name= sheet_name)

