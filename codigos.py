#Primeiramente, coloque a coluna Funcionário como índice;
df = df.set_index('Funcionário')
df

#Saiba que a coluna meses não é necessária para a análise e deve ser retirada;
df = df.drop('Meses', axis = 1)
df

#Qual a média de idade dos funcionários?
df['Anos'].mean()

#Dos funcionários, com filhos, qual o número mais comum?
print(df['Filhos'].mode())

#Qual a média e a mediana dos salários dos funcionários? O que esses valores podem indicar?
l = df['Salário'].mean()
z = df['Salário'].median()
print('A média é:\n', l, '\nA mediana é:\n',z)
#esses valores podem indicar o sálario médio da empresa e o salário que tem maior equilibrio (nem alto e nem baixo)

#Quais são os tipos de instrução existentes?
print(df['Inst.'].unique())

#Qual a média de salário e idade das pessoas casadas?
s = df.loc[df['Est. Cívil'] == 'casado', 'Salário'].mean()
idade = df.loc[df['Est. Cívil'] == 'casado', 'Anos'].mean()
print('A média das idades das pessoas casadas é:\n', idade, '\nA média dos salários é:\n', s)

#Qual o funcionário que possui maior salário (informe seus atributos)?
w = df['Salário'].idxmax()
df.loc[w]

#Qual o funcionário que possui menor idade (informe seus atributos)?
p = df['Anos'].idxmax()
df.loc[p]

#Quem são os funcionários que possuem no máximo 35 anos, são da capital e tem instrução de 2o grau?
df[(df['Anos'] <= 35) &
   (df['Região'] == 'capital') &
   (df['Inst.'] == '2o grau')]

#Faça uma correlação entre todos os atributos. 
#(Dica: mapeie os atributos qualitativos para atributos quantitativos. Ex: solteiro: 1, casado: 2, etc).
#Sem ideia!!!

#Forneça pelo menos mais 3 informações que você achar interessante.
df['Inst.'].count()   # contando qualquer parâmetro, podemos conferir a quantidade total de funcionários.
df[df['Est. Cívil'] == 'casado']  # mostra os funcionários casados e suas informações
df[df['Região'] == 'interior']  # mostra os funcionários que moram no interior e suas informações
