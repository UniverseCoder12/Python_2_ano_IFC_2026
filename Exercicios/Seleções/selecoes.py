class Jogador():
    def __init__(self, pos: str, nm: str, cl: str):
        self.posicao = pos
        self.nome = nm
        self.clube = cl
    
class Selecao():
    def __init__(self, nm: str, ls_j: list):
        self.nome = nm
        self.selecao = ls_j
    
    def jogadores(self):
        jog = ""
        for i in self.selecao:
            jog += f'''Jogador: {i.nome} | Posição: {i.posicao} | Clube: {i.clube}
'''
        return jog
    
    def __str__(self):
        jog = self.jogadores()
        
        return f'''Seleção: {self.nome}
{jog}'''
        
ney_hip = Jogador("Atacante","Neymar Hipotético","Barcelona")
ca_ra = Jogador("Atacante","Caça Rato","Santa Cruz")
bru = Jogador("Goleiro(Matador)","Goleiro Bruno","Presos FC")
pas = Jogador("Zagueiro", "Paspalho", "Time do ovo")
leo_pele = Jogador("Meia", "Léo Pelé", "Hahthlehthicoh Hpharhahnahehnseh")
lis_jog_bra = [ney_hip, ca_ra, bru, pas, leo_pele]
sel_bra = Selecao("Brasil", lis_jog_bra)

print(sel_bra)

im = Jogador("Atacante","Issem","Real Madrid")
mc = Jogador("Atacante","Messi Careca","Carecas FC")
cl = Jogador("Goleiro","Colapinto","Al-mossar")
slh = Jogador("Zagueiro", "Salahda", "Liverpol(URU)")
rd_gr = Jogador("Meia", "Rodrigo Garro", "Time do ovo")
lis_jog_arg = [im, mc, cl, slh, rd_gr]
sel_arg = Selecao("Argentina", lis_jog_arg)

print(sel_arg)