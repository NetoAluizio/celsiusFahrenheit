#!/usr/bin/env python
# coding: utf-8

# In[14]:


while True:                                                 # loço retorna sempre que não é uma entrada válida
    c = input('Informe a temperatura em Celsius: ')
    if c.replace('.', '', 1).replace('-', '', 1).isdigit(): # verifica entrada de dados, inclusive floats e negativos
        c = float(c)                                        # converte entrada em float
        f = ((c*1.8) + 32)
        print(f'A temperatura de {c} graus Celsius equivale(m) a {f:.2f} graus Fahrenheit.')
        break
    else:
        print('Insira só o valor, sem unidades de medida ou vírgulas! O decimal é separado por ponto.')
        continue


# In[ ]:




