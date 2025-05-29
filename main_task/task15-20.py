# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF.


# calculating gross salary
def calc_gross_salary(basic,benefits):
    gross=basic+benefits
    return gross

basic_salary=float(input('Enter basic salary: '))
benefits=float(input('Enter benefits: '))

gross_salary=calc_gross_salary(basic_salary,benefits)
print(gross_salary)

# calculating NHIF
def calc_nhif(summ):
    notes='is your Monthly NHIF contribution'
    if summ<=5999:
        return f'150 {notes}'
    elif summ>=6000 and summ<=7999:
        return f'300 {notes}'
    elif summ>=8000 and summ<=11999:
        return f'400 {notes}'
    elif summ>=12000 and summ<=14999:
        return f'500 {notes}'
    elif summ>=15000 and summ<=19999:
        return f'600 {notes}'
    elif summ>=20000 and summ<=24999:
        return f'750 {notes}'
    elif summ>=25000 and summ<=29999:
        return f'850 {notes}'
    elif summ>=30000 and summ<=34999:
        return f'900 {notes}'
    elif summ>=35000 and summ<=39999:
        return f'950 {notes}'
    elif summ>=40000 and summ<=44999:
        return f'1000 {notes}'
    elif summ>=45000 and summ<=49999:
        return f'1100 {notes}'
    elif summ>=50000 and summ<=59999:
        return f'1200 {notes}'
    elif summ>=60000 and summ<=69999:
        return f'1300 {notes}'
    elif summ>=70000 and summ<=79999:
        return f'1400 {notes}'
    elif summ>=80000 and summ<=89999:
        return f'1500 {notes}'
    elif summ>=90000 and summ<=99999:
        return f'1600 {notes}'
    else:
        return f'1700 {notes}'
    
NHIF=calc_nhif(gross_salary)
print(NHIF)

# calculating NSSF
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 

def calc_nssf(gross,rate=0.06):
    nssf=gross*rate
    return nssf
NSSF = calc_nssf(gross_salary)

def calc_nhdf(gross,rate = 0.015):
    nhdf = gross*rate
    return nhdf
NHDF = calc_nhdf(gross_salary)

# taxable income

def calc_taxable_income(gross,NSSF,NHDF,NHIF):
    taxable_income = gross_salary - (NSSF + NHDF + NHIF)
    return taxable_income

taxable_income = calc_taxable_income(gross_salary,NSSF,NHDF,NHIF)

# PAYE

def calc_payee(taxable_income):
    notes = 'is your payee'
    if taxable_income>=0 and taxable_income<=24000:
        payee = 0
        return f'{payee}{notes}'
    elif taxable_income>24000 and taxable_income<=32333:
        payee = (24000*0.1) + ((taxable_income-24000)*0.25) - 2400
        return f'{payee}{notes}'
    elif taxable_income>32333 and taxable_income<=500000:
        payee = (24000*0.1) + (8333*0.25) + ((taxable_income-32333)*0.3) - 2400
        return f'{payee}{notes}'
    elif taxable_income>500000 and taxable_income<=800000:
        payee = (24000*0.1) + (8333*0.25) + (467667*0.3) + ((taxable_income-500000)*0.325) - 2400
        return f'{payee}{notes}'
    else:
        payee = (24000*0.1) + (8333*0.25) + (467667*0.3) + (300000*0.325) + ((taxable_income - 800000)*0.35) - 2400
        return f'{payee}{notes}'
    
payee = calc_payee(taxable_income)

        


