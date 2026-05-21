# -*- coding: utf-8 -*-
from DrissionPage import Chromium

browser = Chromium()
tab = browser.latest_tab

tab.get("https://example.com")


# =========================================================
# 1. 基础定位：id / class / 标签 / 属性
# =========================================================

# 根据 id 找
ele = tab.ele('css:#loginBtn')
ele = tab.ele('xpath://*[@id="loginBtn"]')


# 根据 class 找
ele = tab.ele('css:.submit-btn')
ele = tab.ele('xpath://*[contains(concat(" ", normalize-space(@class), " "), " submit-btn ")]')


# 根据标签找
ele = tab.ele('css:button')
ele = tab.ele('xpath://button')


# 根据属性找
ele = tab.ele('css:input[name="email"]')
ele = tab.ele('xpath://input[@name="email"]')


# 根据多个属性找
ele = tab.ele('css:input[name="email"][type="text"]')
ele = tab.ele('xpath://input[@name="email" and @type="text"]')


# =========================================================
# 2. class 精确匹配 / class 包含匹配
# =========================================================

# class 完全等于 "123"
ele = tab.ele('css:div[class="123"]')
ele = tab.ele('xpath://div[@class="123"]')


# class 中包含独立类名 "123"
# 可以匹配：class="123"、class="abc 123 def"
# 不会匹配：class="123456"
ele = tab.ele('css:div[class~="123"]')
ele = tab.ele('xpath://div[contains(concat(" ", normalize-space(@class), " "), " 123 ")]')


# class 完全等于 "www"
ele = tab.ele('css:div[class="www"]')
ele = tab.ele('xpath://div[@class="www"]')


# class 中包含独立类名 "www"
ele = tab.ele('css:div[class~="www"]')
ele = tab.ele('xpath://div[contains(concat(" ", normalize-space(@class), " "), " www ")]')


# =========================================================
# 3. 父子节点定位
# =========================================================

# ---------------------------------------------------------
# 3.1 后代节点：父节点下面任意层级的子节点
# ---------------------------------------------------------
# 结构：
# <div class="123">
#     <div>
#         <div class="www"></div>
#     </div>
# </div>

target = tab.ele('css:div[class~="123"] div[class~="www"]')

target = tab.ele(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " 123 ")]'
    '//div[contains(concat(" ", normalize-space(@class), " "), " www ")]'
)


# ---------------------------------------------------------
# 3.2 直接子节点：必须是下一层
# ---------------------------------------------------------
# 结构：
# <div class="123">
#     <div class="www"></div>
# </div>

target = tab.ele('css:div[class~="123"] > div[class~="www"]')

target = tab.ele(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " 123 ")]'
    '/div[contains(concat(" ", normalize-space(@class), " "), " www ")]'
)


# =========================================================
# 4. 兄弟节点定位
# =========================================================

# ---------------------------------------------------------
# 4.1 紧挨着的下一个兄弟节点
# ---------------------------------------------------------
# 结构：
# <div class="123"></div>
# <div class="www"></div>

target = tab.ele('css:div[class~="123"] + div[class~="www"]')

target = tab.ele(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " 123 ")]'
    '/following-sibling::*[1]'
    '[self::div and contains(concat(" ", normalize-space(@class), " "), " www ")]'
)


# ---------------------------------------------------------
# 4.2 后面的某个兄弟节点，不要求紧挨着
# ---------------------------------------------------------
# 结构：
# <div class="123"></div>
# <span>中间隔了一个节点</span>
# <div class="www"></div>

target = tab.ele('css:div[class~="123"] ~ div[class~="www"]')

target = tab.ele(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " 123 ")]'
    '/following-sibling::div[contains(concat(" ", normalize-space(@class), " "), " www ")]'
)


# ---------------------------------------------------------
# 4.3 前面的某个兄弟节点，CSS 不方便，XPath 很方便
# ---------------------------------------------------------
# 结构：
# <div class="label"></div>
# <div class="value"></div>

target = tab.ele(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " value ")]'
    '/preceding-sibling::div[contains(concat(" ", normalize-space(@class), " "), " label ")]'
)


# =========================================================
# 5. 父节点 + 兄弟节点组合
# =========================================================

# 结构：
# <div class="box">
#     <div class="label"></div>
#     <div class="value"></div>
# </div>

# CSS：先锁定 box，再找 label 紧挨着的 value
target = tab.ele('css:div[class~="box"] > div[class~="label"] + div[class~="value"]')

# XPath：同样逻辑
target = tab.ele(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " box ")]'
    '/div[contains(concat(" ", normalize-space(@class), " "), " label ")]'
    '/following-sibling::*[1]'
    '[self::div and contains(concat(" ", normalize-space(@class), " "), " value ")]'
)


# 如果 label 和 value 中间可能隔着其他节点
target = tab.ele('css:div[class~="box"] > div[class~="label"] ~ div[class~="value"]')

target = tab.ele(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " box ")]'
    '/div[contains(concat(" ", normalize-space(@class), " "), " label ")]'
    '/following-sibling::div[contains(concat(" ", normalize-space(@class), " "), " value ")]'
)


# =========================================================
# 6. 更推荐的写法：先锁定父容器，再在里面找
# =========================================================

# ---------------------------------------------------------
# 6.1 CSS 写法
# ---------------------------------------------------------

parent = tab.ele('css:div[class~="123"]')
child = parent.ele('css:div[class~="www"]')

box = tab.ele('css:div[class~="box"]')
target = box.ele('css:div[class~="label"] + div[class~="value"]')


# ---------------------------------------------------------
# 6.2 XPath 写法
# ---------------------------------------------------------

parent = tab.ele(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " 123 ")]'
)

child = parent.ele(
    'xpath:.//div[contains(concat(" ", normalize-space(@class), " "), " www ")]'
)

box = tab.ele(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " box ")]'
)

target = box.ele(
    'xpath:./div[contains(concat(" ", normalize-space(@class), " "), " label ")]'
    '/following-sibling::*[1]'
    '[self::div and contains(concat(" ", normalize-space(@class), " "), " value ")]'
)


# =========================================================
# 7. XPath 特有：向上找父节点 / 祖先节点
# =========================================================

# 结构：
# <tr>
#     <td>A-001</td>
#     <td><button>编辑</button></td>
# </tr>

# 先找到 SKU 所在的 td
sku_td = tab.ele('xpath://td[contains(text(), "A-001")]')

# 向上找最近的 tr
row = sku_td.ele('xpath:./ancestor::tr[1]')

# 在这一行里找编辑按钮
edit_btn = row.ele('xpath:.//button[contains(text(), "编辑")]')

edit_btn.click()


# =========================================================
# 8. XPath 特有：根据文本找元素
# =========================================================

# 精确文本
ele = tab.ele('xpath://button[text()="提交"]')

# 包含文本
ele = tab.ele('xpath://button[contains(text(), "提交")]')

# 任意标签包含文本
ele = tab.ele('xpath://*[contains(text(), "提交")]')


# =========================================================
# 9. 多个元素时
# =========================================================

# ele()：只拿第一个
first_btn = tab.ele('css:button')
first_btn = tab.ele('xpath://button')


# eles()：拿全部
buttons = tab.eles('css:button')
buttons = tab.eles('xpath://button')

for btn in buttons:
    print(btn.text)


# =========================================================
# 10. 电商页面常用：先锁定商品卡片，再找内部按钮
# =========================================================

# CSS 版本
cards = tab.eles('css:div[class~="product-card"]')

for card in cards:
    text = card.text

    if "目标SKU" in text and "在线" in text:
        edit_btn = card.ele('css:button[class~="edit-btn"]')
        edit_btn.click()
        break


# XPath 版本
cards = tab.eles(
    'xpath://div[contains(concat(" ", normalize-space(@class), " "), " product-card ")]'
)

for card in cards:
    text = card.text

    if "目标SKU" in text and "在线" in text:
        edit_btn = card.ele('xpath:.//button[contains(text(), "编辑")]')
        edit_btn.click()
        break


# =========================================================
# 11. 记忆总结
# =========================================================

"""
CSS 关系选择器：

空格   后代节点，下面任意层都可以
>      直接子节点，只能下一层
+      紧挨着的下一个兄弟节点
~      后面的兄弟节点，不要求紧挨着


XPath 关系写法：

//          后代节点，下面任意层都可以
/           直接子节点，只能下一层
following-sibling::*[1]    紧挨着的下一个兄弟节点
following-sibling::div     后面的兄弟节点
preceding-sibling::div     前面的兄弟节点
ancestor::tr[1]            向上找最近的 tr 父级/祖先
.//                         从当前元素内部找后代
./                          从当前元素内部找直接子节点


class 判断：

CSS：
div[class="abc"]      class 完全等于 abc
div[class~="abc"]     class 包含独立类名 abc

XPath：
div[@class="abc"]     class 完全等于 abc

div[contains(concat(" ", normalize-space(@class), " "), " abc ")]
class 包含独立类名 abc，不会误匹配 abc123


最常用模板：

父子：
css:.parent .child
xpath://div[@class="parent"]//div[@class="child"]

直接父子：
css:.parent > .child
xpath://div[@class="parent"]/div[@class="child"]

紧邻兄弟：
css:.label + .value
xpath://div[@class="label"]/following-sibling::*[1][self::div and @class="value"]

后续兄弟：
css:.label ~ .value
xpath://div[@class="label"]/following-sibling::div[@class="value"]

向上找父级：
xpath:./ancestor::tr[1]
"""
