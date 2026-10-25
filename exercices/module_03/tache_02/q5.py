bonbons = 53
eleves = 8

part = bonbons // eleves
reste = bonbons % eleves

print(f"Chaque élève reçoit {part} bonbons.")
print(f"Il reste {reste} bonbons.")
print(f"Avec /, 53 / 8 = {bonbons / eleves} : la part peut être décimale.")
print("Avec // et %, chaque part reste entière et le reste indique les bonbons non distribués.")
