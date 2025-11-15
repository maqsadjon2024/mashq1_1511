# 1-misol
class Transport:
    def __init__(self, nomi, tezlik=0):
        self.nomi = nomi
        self.tezlik = tezlik

    def tezlik_oshirish(self):
        """Har transport o‘zicha tezlik oshiradi (polimorfizm)."""
        raise NotImplementedError

    def yoqilg_sarfi(self):
        """Har transport turlicha yoqilg‘i sarf qiladi."""
        raise NotImplementedError

    def sayohat_masofa(self, masofa):
        """
        Masofa berilganda vaqt va yoqilg‘i sarfi qaytaradi.
        vaqt = masofa / tezlik
        yoqilg‘i = masofa * sarf
        """
        sarf = self.yoqilg_sarfi()
        vaqt = masofa / self.tezlik
        yoqilg = masofa * sarf
        return vaqt, yoqilg

    def yuk_kotarish(self, yuk):
        """Faqat YukMashina override qiladi"""
        return 0


class Avtobus(Transport):
    def tezlik_oshirish(self):
        self.tezlik += 10
        return self.tezlik

    def yoqilg_sarfi(self):
        return 0.25   


class SportAvto(Transport):
    def tezlik_oshirish(self):
        self.tezlik += 30
        return self.tezlik

    def yoqilg_sarfi(self):
        return 0.4     


class YukMashina(Transport):
    def tezlik_oshirish(self):
        self.tezlik += 5
        return self.tezlik

    def yoqilg_sarfi(self):
        return 0.6     

    def yuk_kotarish(self, yuk):
        return f"{self.nomi} {yuk} tonna yuk ko‘tardi"


park = [
    Avtobus("MAN avtobusi", 60),
    YukMashina("Kamaz", 40),
    SportAvto("BMW M5", 120)
]

masofa = 100  

for t in park:
    vaqt, yoqilg = t.sayohat_masofa(masofa)
    print(f"{t.nomi}: {masofa} km uchun vaqt={vaqt:.2f} soat, yoqilg‘i={yoqilg:.1f} litr")

    # Yuk ko‘tarish test
    print("Yuk ko‘tarish:", t.yuk_kotarish(5))
    print("------------------------")
