#conversor de temperatura
temperatura_Celsius =  float(input("Digite a temperatura em Celsius e eu converterei em Fahrenheit"))
temperatura_Fahrenheit = (temperatura_Celsius * 9/5)+ 32
print("A temperatura em Celsius  {:.2f}".format(temperatura_Celsius) + " ºC convertida em Fahreint é {:.2f}".format(temperatura_Fahrenheit)+ "ºF")