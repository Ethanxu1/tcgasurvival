#!/usr/bin/python3  

# Import modules for CGI handling
import cgi, cgitb

import cgitb; cgitb.enable()

import os
# Create instance of FieldStorage
form = cgi.FieldStorage()

cohort = ''
if form.getvalue('cohort'):
    cohort = form.getvalue('cohort')
else:
    cohort = 'no value found'

print()

with open('header.html') as f:
    lines = f.readlines()
    for i in lines:
        print(i, end='')
    f.close()

print (
f'''
<h3>RNASeq gene expression survival plots</h3>
<form action=\"../../../cgi-bin/tcgasurvival/survivalfig.py\" method=\"POST\">
    <table summary=\"RNASeq expression profile\" class=nonbordered>
        <tr>
            <td>
                <label for=\"cohort\"><b>Cohort:</b></label>

                <select name=\"cohort\" id="cohort">
                <option value="{cohort}">{cohort}</option>
                <option value="ACC">ACC</option>
                <option value="BLCA">BLCA</option>
                <option value="BRCA">BRCA</option>
                <option value="CESC">CESC</option>
                <option value="CHOL">CHOL</option>
                <option value="COAD">COAD</option>
                <option value="COADREAD">COADREAD</option>
                <option value="DLBC">DLBC</option>
                <option value="ESCA">ESCA</option>
                <option value="GBM">GBM</option>
                <option value="GBMLGG">GBMLGG</option>
                <option value="HNSC">HNSC</option>
                <option value="KICH">KICH</option>
                <option value="KIPAN">KIPAN</option>
                <option value="KIRC">KIRC</option>
                <option value="KIRP">KIRP</option>
                <option value="LAML">LAML</option>
                <option value="LGG">LGG</option>
                <option value="LIHC">LIHC</option>
                <option value="LUAD">LUAD</option>
                <option value="LUSC">LUSC</option>
                <option value="MESO">MESO</option>
                <option value="OV">OV</option>
                <option value="PAAD">PAAD</option>
                <option value="PCPG">PCPG</option>
                <option value="PRAD">PRAD</option>
                <option value="READ">READ</option>
                <option value="SARC">SARC</option>
                <option value="SKCM">SKCM</option>
                <option value="STAD">STAD</option>
                <option value="STES">STES</option>
                <option value="TGCT">TGCT</option>
                <option value="THCA">THCA</option>
                <option value="THYM">THYM</option>
                <option value="UCEC">UCEC</option>
                <option value="UCS">UCS</option>
                <option value="UVM">UVM</option>
                </select>

                <label for=\"gene\"> 
                    <b>Gene or Gene id:</b> 
                </label>
                <input type=\"text\" name=\"gene\" value=\"\" title=\"gene\" size=20 id=\"gene\">
                <input type=\"submit\" title=\"Submit\" aria-label=\"Submit\" value=\"Survival Plots\">
            </td>
        </tr>
    </table>
</form>
'''
)
with open('footer.html') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')
