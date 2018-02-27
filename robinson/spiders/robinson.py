import scrapy


class RobinsonSpider(scrapy.Spider):
    name = 'robinson'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.games = []
        self.data = {}

    def start_requests(self):
        url = "https://expeditierobinson.rtl.nl/"
        yield scrapy.Request(url=url, callback=self.build_urls)

    def build_urls(self, response):
        id_url = response.css(".holder-persons").css("a").xpath("@href").extract_first().strip("/profiel/")
        range_end = int(id_url) + 20
        urls = []
        for x in range(0, range_end):
            urls.append("https://expeditierobinson.rtl.nl/profiel/{}".format(x))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response is not None:
            url = response.url
            naam = response.css(".holder-bio").css("h2").css("::text").extract_first().strip()
            single_data = {"url": url}
            if not response.css(".votes"):
                return
            games = response.css(".item-video")
            for game in games:
                game_naam = game.css(".text-subtitle").css("::text").extract_first().strip()
                game_stemmen = game.css(".votes").css("::text").extract_first().strip(" stemmen")
                if game_naam not in self.games:
                    self.games.append(game_naam)
                single_data[game_naam] = game_stemmen
            self.data[naam] = single_data

    def closed(self, reason):
        self.export_data()

    def export_data(self):
        with open("export.tsv", "w") as file:
            file.write("Naam\tUrl")
            for game in self.games:
                file.write("\t")
                file.write(game)
            file.write("\n")

            for naam in self.data.keys():
                url = self.data[naam]["url"]
                file.write("{}\t{}".format(naam, url))
                for game in self.games:
                    votes = 0;
                    if game in self.data[naam]:
                        votes = self.data[naam][game]
                    file.write("\t{}".format(votes))
                file.write("\n")