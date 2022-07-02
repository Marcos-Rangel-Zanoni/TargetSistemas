vet =[];
i = 1;
x = 1;


while i <= 30:
    resp = float(input("\n>"));
    vet.append(resp);

    i += 1;
    

me= min(vet);
ma = max(vet);
dias = 0;
total = 0;
i_media = [];

for x in range(len(vet)):
    if vet[x] > 0.0:
        total += vet[x];
        dias += 1;
        



media = total / dias;


for i in range(len(vet)):
    if vet[i] > media:
        i_media.append(i+1);
        
print(f"Maior Valor de faturamento ocorrido foi de {ma}");
print(f"Menor valor de faturamento ocorrido foi de {me}");
print(f"Dias no mês em que o valor de faturamento diário fou superior à média mensal:{i_media}");

