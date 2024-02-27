import time

import uiautomator2 as u2
from uiautomator2 import Direction
device_id = 'emulator-5554'
# device_id = 'TSBM9L55QWWG4LIR'
u = u2.connect(device_id)
u = u2.connect()
print(u.info)
# d = u.session('ru.limeshop.android.dev')


u.implicitly_wait(10)
u.swipe_ext(Direction.FORWARD)  # вверх
u.swipe_ext(Direction.BACKWARD)  # вниз
u.swipe_ext(Direction.HORIZ_FORWARD)  # влево
u.swipe_ext(Direction.HORIZ_BACKWARD)  # вправо
# d(resourceId="ru.limeshop.android.dev:id/nav_catalog_menu").click()
# d(resourceId="ru.limeshop.android.dev:id/catalog_item_name", text="РАСПРОДАЖА").click()
# d(resourceId="ru.limeshop.android.dev:id/catalog_item_name", text="БРЮКИ").click()
# d.xpath(
#         '//android.widget.TableLayout/android.widget.TableRow[1]/'
#         'android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
# name_pr1 = d(resourceId="ru.limeshop.android.dev:id/nameTextView",
#                  text="БРЮКИ ЗАУЖЕННОГО КРОЯ С ЗАЩИПАМИ").get_text()
# d.xpath('//android.widget.ImageButton').click()
# d.xpath('//*[@resource-id="ru.limeshop.android.dev:id/notification_negative_button"]').click()
# d.xpath('//android.widget.ImageButton').click()
# d(resourceId="ru.limeshop.android.dev:id/nav_favorites").click()
# name_pr2 = d(resourceId="ru.limeshop.android.dev:id/item_product_name").get_text()
# assert name_pr1 == name_pr2, 'Наименования товаров не совпадают'


u.app_stop('ru.limeshop.android.dev')
