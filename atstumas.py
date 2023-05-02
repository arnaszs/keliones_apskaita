
def skaiciuokle(values):
    try:
        atstumas = float(values['atstumas'])
        sanaudos = float(values['sanaudos'])
        talpa = float(values['talpa'])
        kuro_kaina = 1.5  # Example fuel price
        kaina = (atstumas / 100) * sanaudos * kuro_kaina
        if kaina > 0:
            liko_km = talpa / sanaudos * 100 - atstumas
            if liko_km > 0:
                output_str = f'Kelionė kainuos {kaina:.2f}€. Liko kuro {liko_km:.1f}km'
            else:
                output_str = f'Kelionė kainuos {kaina:.2f}€. Kuro neužteks iki paskirties vietos.'
        else:
            output_str = 'Įveskite teisingus skaičius.'
    except ValueError:
        output_str = 'Įveskite teisingus skaičius.'
