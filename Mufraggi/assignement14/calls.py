class Calls():
    def __init__(self, last, net, bib, ask, vol, IV, delta, gamma, int):
        self.last = last
        self.net = net
        self.bib = bib
        self.ask = ask
        self.vol = vol
        self.IV = IV
        self.delta = delta
        self.gamma = gamma
        self.int = int

    def print_data(self):
        for i in range(len(self.last)):
            print(self.last[i])
            print(self.net[i])
            print(self.bib[i])
            print(self.ask[i])
            print(self.vol[i])
            print(self.IV[i])
            print(self.delta[i])
            print(self.gamma[i])
            print(self.int[i])

def init_element(list):
    last_list = []
    net_list = []
    bib_list = []
    ask_list = []
    vol_list = []
    IV_list = []
    delta_list = []
    gamma_list = []
    int_list = []
    for element in list:
        element = element.split(' ')
        last_list.append(element[0])
        net_list.append(element[1])
        bib_list.append(element[2])
        ask_list.append(element[3])
        vol_list.append((element[4]))
        IV_list.append(element[5])
        delta_list.append(element[6])
        gamma_list.append(element[7])
        int_list.append(element[8])
    return Calls(last=last_list, net=net_list, bib=bib_list, ask=ask_list, vol=vol_list, IV=IV_list, delta=delta_list,
                 gamma=gamma_list, int=int_list)
