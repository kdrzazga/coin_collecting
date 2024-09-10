import translator
from shop import Shop


class HalloweenShop(Shop):
    def __init__(self, language):
        super().__init__(language)
        self.add_item(Shop.Item(translator.pumpkin[language], 10, translator.yellow_skin_description[language],
                                'resources/images/item_icons/pumpkin.png'))
