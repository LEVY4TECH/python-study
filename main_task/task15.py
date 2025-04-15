# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 


def nhif(salary,benefits):
    summ=salary+benefits
    print(summ)
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
    

salary=float(input('Enter your basic salary: '))
benefits=float(input('Enter your allowances: '))

x=nhif(salary,benefits)
print(x)