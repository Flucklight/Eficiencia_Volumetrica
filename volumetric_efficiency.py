import matplotlib.pyplot as plt


def fragment(n):
    r = n % 1024
    m = (n - r) / 1024
    fragments = [int(m), r]
    return fragments


def volumetric_efficiency(message):
    data = fragment(message)

    tcp = 0
    ip = 0
    llc = 0
    ma_pdu = 0

    if data[1] != 0:
        tcp = data[1] + 20
        ip = tcp + 20
        llc = ip + 3
        ma_pdu = llc + 18

    tcp_efficiency = (message/(tcp + ((1024 + 20) * data[0]))) * 100
    ip_efficiency = (message/(ip + ((1044 + 20) * data[0]))) * 100
    llc_efficiency = (message/(llc + ((1064 + 3) * data[0]))) * 100
    efficiency = (message/(ma_pdu + ((1067 + 18) * data[0]))) * 100

    protocol = {'message': message, 'tcp': round(tcp_efficiency, ndigits=2),
                'ip': round(ip_efficiency, ndigits=2), 'llc': round(llc_efficiency, ndigits=2),
                'efficiency': round(efficiency, ndigits=2)}
    return protocol


plt.ylabel('eficiencia')
plt.xlabel('mensaje')
data = []
plot_x = []
plot_tcp = []
plot_ip = []
plot_llc = []
plot_efficiency = []
for i in range(1, 1001):
    data.append(volumetric_efficiency(i * 5))
for d in data:
    print(d)
    plot_x.append(d['message'])
    plot_tcp.append(d['tcp'])
    plot_ip.append(d['ip'])
    plot_llc.append(d['llc'])
    plot_efficiency.append(d['efficiency'])
plt.plot(plot_x, plot_tcp)
plt.plot(plot_x, plot_ip)
plt.plot(plot_x, plot_llc)
plt.plot(plot_x, plot_efficiency)
plt.show()
