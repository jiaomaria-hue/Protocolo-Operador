comp_piso = float(input('Comprimento do ambiente (m): '))
larg_piso = float(input('Largura do ambiente (m): '))
area_peca = float(input('Área de UMA peça de cerâmica (m²): '))

area_total = comp_piso * larg_piso

# Adicionando 10% de margem de quebra
# Multiplicamos por 1.10 para ter segurança
qtd_pecas = (area_total * 1.10) / area_peca

print(f'Para uma área de {area_total:.2f}m², você precisará de {qtd_pecas:.0f} peças.')