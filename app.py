from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


TEXTS = {
    "en": {
        "site_title": "Hangzhou Green Leaf Tea | Premium Chinese Green Tea for Export",
        "brand": "Green Leaf Tea",

        # NAV
        "nav_story": "Our Story",
        "nav_products": "Teas",
        "nav_craft": "Craft",
        "nav_wholesale": "Wholesale",
        "nav_reviews": "Reviews",
        "nav_order": "How to Order",
        "nav_contact": "Contact",

        # HERO
        "hero_badge_location": "Hangzhou · West Lake Region · China",
        "hero_title": "Premium Green Tea from the Hills of Hangzhou",
        "hero_sub": (
            "Hangzhou Green Leaf Tea offers carefully selected Chinese green teas directly from our partner "
            "gardens in the West Lake region. We supply specialty stores, tea brands and cafés around the world "
            "with consistent quality and reliable export service."
        ),
        "hero_cta1": "Request Price List",
        "hero_cta2": "Explore Tea Collection",
        "hero_chip1": "Loose leaf · Whole leaf",
        "hero_chip2": "Private label & OEM",
        "hero_chip3": "Food safety documents",
        "hero_quick_title": "Quick export facts",
        "hero_fact1_num": "10+ years",
        "hero_fact1_label": "Export experience",
        "hero_fact2_num": "20+ countries",
        "hero_fact2_label": "Europe, N. America, Asia",
        "hero_fact3_num": "Low MOQ",
        "hero_fact3_label": "For new partners",
        "hero_fact4_num": "Flexible packing",
        "hero_fact4_label": "Retail or bulk",
        "hero_demo_note": (
            "This is a demo website used to show the style of export websites we can build "
            "for tea brands and food producers in China."
        ),

        # STORY
        "section_story_label": "Our Story",
        "section_story_title": "From Hangzhou Hills to Cups Around the World",
        "story_p1": (
            "Hangzhou Green Leaf Tea works closely with small and medium-sized tea gardens "
            "in the West Lake and surrounding mountain areas. We select batches based on freshness, "
            "leaf appearance, aroma and taste, and then process and pack them according to the needs "
            "of our overseas customers."
        ),
        "story_p2": (
            "Whether you are a specialty tea shop, a café chain, or a growing tea brand, "
            "we help you source consistent quality Chinese green tea with clear communication "
            "and export-friendly documentation."
        ),
        "story_box1_title": "Origin Control",
        "story_box1_text": (
            "Partner gardens in selected areas with traceability and stable harvests."
        ),
        "story_box2_title": "Blending & Customization",
        "story_box2_text": (
            "Support for custom blends, flavor profiles and private label concepts."
        ),
        "story_img_alt": "Tea garden in Hangzhou hills",

        # PRODUCTS
        "section_products_label": "Tea Collection",
        "section_products_title": "Selected Green Teas for Overseas Markets",
        "section_products_sub": "Loose leaf · Retail tins · Foodservice packs",

        "prod1_tag": "Signature Origin",
        "prod1_title": "West Lake Longjing",
        "prod1_text": (
            "Hand-picked early spring leaves from selected Longjing areas near West Lake. "
            "Classic chestnut aroma, smooth taste and bright liquor color."
        ),
        "prod1_li1": "Harvest: early spring (pre-Qingming / pre-rain)",
        "prod1_li2": "Grades for premium retail and gifting",
        "prod1_li3": "Packaging: tins, gift boxes, bulk foil bags",
        "prod1_note": "Ideal for specialty tea shops and high-end gift lines.",
        "prod1_img_alt": "Longjing green tea",

        "prod2_tag": "Daily Favorite",
        "prod2_title": "Maofeng Green Tea",
        "prod2_text": (
            "A balanced, fragrant green tea suitable for daily drinking, with multiple "
            "infusions and good value for money."
        ),
        "prod2_li1": "Stable quality and large volume supply",
        "prod2_li2": "Ideal for foodservice and house blends",
        "prod2_li3": "Packaging: 250 g / 500 g / 1 kg bags",
        "prod2_note": "Popular with cafés and restaurants as house green tea.",
        "prod2_img_alt": "Maofeng green tea",

        "prod3_tag": "Custom Concept",
        "prod3_title": "Custom Green Tea Blends",
        "prod3_text": (
            "Tailor-made blends and flavored teas to match your brand story, "
            "target market and price point."
        ),
        "prod3_li1": "Support for flavored & scented teas",
        "prod3_li2": "Consultation on flavor trends in your market",
        "prod3_li3": "Private label and design support",
        "prod3_note": (
            "Designed together with your team for retail or online channels."
        ),
        "prod3_img_alt": "Custom tea blends",

        "products_cta_button": "Ask for Detailed Specification & Samples",
        "products_cta_hint": (
            "Tell us your target market, retail price range and desired taste profile."
        ),

        # CRAFT
        "section_craft_label": "Craft & Control",
        "section_craft_title": "How We Work with Tea – From Fresh Leaf to Packed Product",
        "craft_p1": (
            "Our role is to connect traditional tea craftsmanship with modern export requirements. "
            "We work with selected producers and monitor critical steps in the process to keep "
            "quality consistent from batch to batch."
        ),
        "craft_step1_title": "Garden & Harvest Selection",
        "craft_step1_text": (
            "Selection of origin, altitude and plucking standard according to your "
            "quality and price needs."
        ),
        "craft_step2_title": "Processing & Tasting",
        "craft_step2_text": (
            "Coordination with tea makers, sample roasting and regular cuppings "
            "to confirm aroma, liquor color and mouthfeel."
        ),
        "craft_step3_title": "Packaging & Food Safety",
        "craft_step3_text": (
            "Selection of suitable packaging materials, labeling according to your "
            "regulations and preparation of documents."
        ),
        "craft_step4_title": "Export & Logistics",
        "craft_step4_text": (
            "Coordination of inspection, loading and shipment from ports near "
            "Shanghai or Ningbo, with transparent communication on timing."
        ),
        "craft_box_title": "Documents We Commonly Provide",
        "craft_box_li1": "Product specification sheets (per SKU)",
        "craft_box_li2": (
            "Basic microbiological and pesticide residue test reports (through third parties)"
        ),
        "craft_box_li3": "Ingredient lists and allergen statements",
        "craft_box_li4": "Packing list, commercial invoice and certificate of origin",
        "craft_box_note": (
            "The exact set of documents depends on your country and channel "
            "(retail, online, foodservice). We can discuss these details before "
            "confirming the order."
        ),

        # WHOLESALE
        "section_wh_label": "Wholesale & B2B",
        "section_wh_title": "For Tea Shops, Cafés, Importers and Brands",
        "wh_col1_title": "Specialty Tea Shops",
        "wh_col1_text": (
            "Carefully selected teas for your loose leaf counters and gift tins. "
            "Support for sampling, storytelling and point-of-sale material ideas."
        ),
        "wh_col2_title": "Cafés & Restaurants",
        "wh_col2_text": (
            "Stable daily-drinking quality for foodservice, "
            "with packing suitable for back-of-house operations."
        ),
        "wh_col3_title": "Private Label & Online Brands",
        "wh_col3_text": (
            "Custom blends, flexible MOQs, and support for packaging concepts "
            "aimed at your customers."
        ),
        "wh_note": (
            "We usually start with smaller trial orders to fine-tune teas and packaging "
            "before moving to regular shipments."
        ),

        # REVIEWS
        "section_reviews_label": "What Our Partners Say",
        "section_reviews_title": "Selected Feedback from Overseas Customers",
        "rev1_text": (
            "“The Longjing we receive each spring is consistent and our customers notice "
            "the freshness. Communication about harvest timing and pricing is clear.”"
        ),
        "rev1_role": "Tea shop owner",
        "rev1_loc": "Germany · Loose leaf retailer",
        "rev2_text": (
            "“For our café chain we needed a simple, good green tea with stable taste. "
            "Green Leaf Tea helped us choose a Maofeng grade that fits our price range.”"
        ),
        "rev2_role": "Beverage manager",
        "rev2_loc": "Middle East · Café group",
        "rev3_text": (
            "“We developed a custom blend for our online brand together, including "
            "flavor testing and packaging ideas. The process was structured and transparent.”"
        ),
        "rev3_role": "Brand founder",
        "rev3_loc": "USA · Online tea brand",
        "reviews_note": (
            "These are sample quotes used to illustrate how real feedback can be shown on an export website."
        ),

        # ORDER
        "section_order_label": "How to Order",
        "section_order_title": "Simple Steps to Start Working Together",
        "order_box1_title": "1. Tell Us About Your Project",
        "order_box1_text": (
            "Share your target market, channels (offline / online), expected retail price range "
            "and any teas you are already selling."
        ),
        "order_box2_title": "2. Receive Suggestions & Samples",
        "order_box2_text": (
            "We recommend suitable teas and send samples. You taste them, "
            "collect feedback and choose preferred options."
        ),
        "order_box3_title": "3. Confirm Packaging & Documents",
        "order_box3_text": (
            "We agree on packaging format, labeling requirements and needed food safety documents."
        ),
        "order_box4_title": "4. Place Order & Arrange Shipment",
        "order_box4_text": (
            "After deposit, we prepare your teas, pack them, arrange inspection if needed, "
            "and ship from a nearby port."
        ),
        "order_note": (
            "For new partners, we usually recommend starting with a smaller mixed order "
            "to test teas and the market."
        ),
        "order_right_title": "Basic Payment & Terms (Sample Demo)",
        "order_right_li1": "New customers: 30% deposit, 70% before shipment (T/T)",
        "order_right_li2": "Existing partners: flexible options to discuss",
        "order_right_li3": (
            "Samples: cost + courier fee (deductible from first order in many cases)"
        ),
        "order_right_note": (
            "Exact payment terms can be adjusted depending on volume, frequency and your standard practice."
        ),

        # CONTACT
        "section_contact_label": "Contact",
        "section_contact_title": "Let's Talk About Tea for Your Market",
        "contact_p": (
            "For inquiries, please send us a short introduction of your company, channels and what kind "
            "of teas you are interested in. We will reply with suggestions and basic price indications."
        ),
        "contact_company_label": "Company:",
        "contact_company_value": "Hangzhou Green Leaf Tea (Demo)",
        "contact_location_label": "Location:",
        "contact_location_value": "Hangzhou, Zhejiang, China",
        "contact_email_label": "Email:",
        "contact_email_value": "export@greenleaf-demo.com",
        "contact_phone_label": "WeChat / Phone:",
        "contact_phone_value": "+86-000-0000-0000",
        "contact_wechat_demo": "WeChat QR (demo):",
        "contact_footer_note": (
            "This website is a sample created to demonstrate how an export-focused brand website "
            "can look for tea and food products from China."
        ),
        "contact_qr_alt": "WeChat QR code",

        # CONTACT FORM
        "form_name_label": "Your Name",
        "form_name_placeholder": "Your full name",
        "form_company_label": "Company",
        "form_company_placeholder": "Company name",
        "form_country_label": "Country / Market",
        "form_country_placeholder": "e.g. Germany, UAE, USA",
        "form_email_label": "Email",
        "form_email_placeholder": "you@example.com",
        "form_message_label": "Tell us about your project",
        "form_message_placeholder": (
            "Your channels, price range, teas you are looking for..."
        ),
        "form_submit": "Send Inquiry",
    },

    "zh": {
        "site_title": "杭州绿叶茶 | 中国出口绿茶示例网站",
        "brand": "Green Leaf Tea",

        # NAV
        "nav_story": "品牌故事",
        "nav_products": "茶品",
        "nav_craft": "工艺",
        "nav_wholesale": "批发合作",
        "nav_reviews": "客户评价",
        "nav_order": "合作流程",
        "nav_contact": "联系我们",

        # HERO
        "hero_badge_location": "杭州 · 西湖产区 · 中国",
        "hero_title": "来自杭州茶山的优质绿茶",
        "hero_sub": (
            "杭州绿叶茶与西湖及周边山地的合作茶园紧密合作，精选优质中国绿茶，"
            "直接出口至全球各地的茶叶店、品牌商和咖啡馆，为您提供稳定品质和可靠的出口服务。"
        ),
        "hero_cta1": "索取价格表",
        "hero_cta2": "查看茶品系列",
        "hero_chip1": "散茶 · 整片茶叶",
        "hero_chip2": "自有品牌 & OEM",
        "hero_chip3": "食品安全文件支持",
        "hero_quick_title": "出口关键信息",
        "hero_fact1_num": "10+ 年",
        "hero_fact1_label": "出口经验",
        "hero_fact2_num": "20+ 国家",
        "hero_fact2_label": "欧洲 · 北美 · 亚洲",
        "hero_fact3_num": "起订量灵活",
        "hero_fact3_label": "适合新合作伙伴",
        "hero_fact4_num": "多种包装",
        "hero_fact4_label": "零售或散装",
        "hero_demo_note": (
            "本网站为演示页面，用于展示我们可以为中国茶叶品牌和食品企业制作的出口型网站风格。"
        ),

        # STORY
        "section_story_label": "品牌故事",
        "section_story_title": "从杭州茶山走向世界茶杯",
        "story_p1": (
            "杭州绿叶茶与西湖及周边山区的中小型茶园长期合作，"
            "根据新鲜度、外形、香气和口感精挑细选茶叶批次，"
            "并按海外客户的需求进行进一步加工和包装。"
        ),
        "story_p2": (
            "无论您是精品茶叶店、咖啡连锁，还是成长中的茶叶品牌，"
            "我们都可以通过清晰的沟通和适合出口的文件支持，"
            "帮助您稳定采购优质的中国绿茶。"
        ),
        "story_box1_title": "产地与来源控制",
        "story_box1_text": "精选可追溯、产量稳定的合作茶园，保证原料来源可靠。",
        "story_box2_title": "拼配与定制",
        "story_box2_text": "支持按口味、价格定位和品牌故事进行定制拼配与开发。",
        "story_img_alt": "杭州茶山茶园风景",

        # PRODUCTS
        "section_products_label": "茶品系列",
        "section_products_title": "适合海外市场的精选绿茶",
        "section_products_sub": "散茶 · 礼盒罐装 · 餐饮大包装",

        "prod1_tag": "核心产区",
        "prod1_title": "西湖龙井",
        "prod1_text": (
            "采自西湖周边精选龙井产区的早春嫩叶，"
            "香气清雅带炒豆香，滋味鲜爽顺滑，汤色明亮。"
        ),
        "prod1_li1": "采摘时间：早春（清明前 / 雨前）",
        "prod1_li2": "适合高档零售和礼品渠道的多个等级",
        "prod1_li3": "包装形式：铁罐、礼盒、铝箔散装袋等",
        "prod1_note": "适合精品茶叶店和中高端礼盒系列。",
        "prod1_img_alt": "西湖龙井绿茶",

        "prod2_tag": "日饮优选",
        "prod2_title": "毛峰绿茶",
        "prod2_text": (
            "香气清新、口感平衡，适合日常饮用，可多次冲泡，性价比高。"
        ),
        "prod2_li1": "质量稳定，供货量大，适合长期合作",
        "prod2_li2": "非常适合餐饮和自有招牌绿茶",
        "prod2_li3": "包装形式：250 克 / 500 克 / 1 千克袋装",
        "prod2_note": "深受咖啡馆和餐厅作为店用绿茶的欢迎。",
        "prod2_img_alt": "毛峰绿茶",

        "prod3_tag": "定制方案",
        "prod3_title": "定制绿茶拼配",
        "prod3_text": (
            "根据您的品牌故事、目标市场和价格区间，"
            "共同设计专属的绿茶拼配及风味型产品。"
        ),
        "prod3_li1": "支持调味茶、花香茶等风味开发",
        "prod3_li2": "结合您所在市场的口味趋势提供建议",
        "prod3_li3": "提供自有品牌和包装设计配合",
        "prod3_note": "可与您团队共同开发适合零售或线上销售的系列产品。",
        "prod3_img_alt": "定制绿茶拼配",

        "products_cta_button": "索取详细规格及样品方案",
        "products_cta_hint": "请告知目标市场、零售价格区间及期望的口味风格。",

        # CRAFT
        "section_craft_label": "工艺与把控",
        "section_craft_title": "从鲜叶到成品包装 · 我们如何把控茶叶",
        "craft_p1": (
            "我们的角色是把传统制茶工艺与现代出口要求相结合，"
            "与精选茶企合作，关注加工过程中的关键环节，"
            "确保不同批次之间的质量尽量保持稳定。"
        ),
        "craft_step1_title": "茶园及采摘标准选择",
        "craft_step1_text": "根据您的品质及价格需求选择产地、海拔和采摘标准。",
        "craft_step2_title": "加工与品评",
        "craft_step2_text": (
            "与制茶师沟通火候与工艺，通过样品炒制和定期品评，"
            "确认香气、汤色和口感。"
        ),
        "craft_step3_title": "包装与食品安全",
        "craft_step3_text": (
            "根据您的法规要求选择合适的包装材料及标签形式，"
            "并提前准备相关文件。"
        ),
        "craft_step4_title": "出口与物流",
        "craft_step4_text": (
            "协调检验、装柜与出运，通常从上海或宁波附近港口发货，"
            "并保持透明的时间沟通。"
        ),
        "craft_box_title": "常见可提供的文件",
        "craft_box_li1": "每个 SKU 的产品规格书",
        "craft_box_li2": "通过第三方机构出具的基本微生物与农残检测报告",
        "craft_box_li3": "配料表及过敏原说明",
        "craft_box_li4": "装箱单、商用发票、原产地证等",
        "craft_box_note": (
            "具体所需文件会根据您的国家及销售渠道（零售、线上、餐饮）而定，"
            "可在下单前一起确认。"
        ),

        # WHOLESALE
        "section_wh_label": "批发与 B2B",
        "section_wh_title": "面向茶叶店、咖啡馆、进口商及品牌方",
        "wh_col1_title": "精品茶叶店",
        "wh_col1_text": (
            "为散茶柜台和礼盒罐装精选茶叶，支持样品寄送、故事撰写"
            "及线下陈列物料的创意。"
        ),
        "wh_col2_title": "咖啡馆与餐厅",
        "wh_col2_text": (
            "适合日常饮用的稳定品质绿茶，"
            "包装形式便于后厨储存和使用。"
        ),
        "wh_col3_title": "自有品牌与线上品牌",
        "wh_col3_text": (
            "提供定制拼配、灵活起订量及包装方案，"
            "帮助您打造面向终端消费者的产品系列。"
        ),
        "wh_note": (
            "通常建议先通过较小的试订单测试茶品及包装，"
            "再逐步转为常规出货。"
        ),

        # REVIEWS
        "section_reviews_label": "合作伙伴评价",
        "section_reviews_title": "来自海外客户的部分反馈示例",
        "rev1_text": (
            "“我们每年春季收到的龙井质量稳定，顾客能明显感到新鲜度。"
            "关于采摘时间和价格的沟通也很及时清晰。”"
        ),
        "rev1_role": "茶叶店老板",
        "rev1_loc": "德国 · 散茶零售商",
        "rev2_text": (
            "“我们的咖啡连锁需要一款简单但稳定的绿茶。"
            "绿叶茶帮助我们选定了一款符合价格区间的毛峰等级。”"
        ),
        "rev2_role": "饮品经理",
        "rev2_loc": "中东 · 咖啡连锁",
        "rev3_text": (
            "“我们与绿叶茶一起开发了线上品牌的定制拼配，"
            "包括风味测试和包装创意，整个过程清晰而有条理。”"
        ),
        "rev3_role": "品牌创始人",
        "rev3_loc": "美国 · 线上茶叶品牌",
        "reviews_note": "以上为示例性评价，用于展示出口网站上可呈现的真实反馈形式。",

        # ORDER
        "section_order_label": "合作流程",
        "section_order_title": "与我们合作的简单步骤",
        "order_box1_title": "1. 介绍您的项目",
        "order_box1_text": (
            "请简要说明目标市场、销售渠道（线下 / 线上）、"
            "预计零售价格区间以及目前已有的茶品情况。"
        ),
        "order_box2_title": "2. 收到方案与样品",
        "order_box2_text": (
            "我们会推荐合适的茶品并寄送样品，"
            "您进行品评并收集反馈，最终选出优先方案。"
        ),
        "order_box3_title": "3. 确认包装与文件",
        "order_box3_text": (
            "就包装形式、标签要求以及所需食品安全文件达成一致。"
        ),
        "order_box4_title": "4. 下单生产与安排出货",
        "order_box4_text": (
            "在收到订金后安排备茶、包装、必要时的检验，"
            "并从附近港口发货。"
        ),
        "order_note": (
            "对于新合作伙伴，我们通常建议以较小的组合订单开始，"
            "以便测试产品和市场反应。"
        ),
        "order_right_title": "基本付款条款（演示）",
        "order_right_li1": "新客户：预付 30% 订金，出货前付清 70% 余款（电汇）",
        "order_right_li2": "老客户：可根据合作情况灵活协商条款",
        "order_right_li3": "样品：样品费 + 快递费（通常可在首单中抵扣）",
        "order_right_note": (
            "具体付款方式可根据订单金额、频率以及您的常规做法进行调整。"
        ),

        # CONTACT
        "section_contact_label": "联系",
        "section_contact_title": "欢迎与我们讨论适合您市场的中国绿茶",
        "contact_p": (
            "如需询盘，请简单介绍您的公司背景、销售渠道以及感兴趣的茶类，"
            "我们会给出相应建议和基本价格区间。"
        ),
        "contact_company_label": "公司：",
        "contact_company_value": "杭州绿叶茶（演示）",
        "contact_location_label": "地址：",
        "contact_location_value": "中国浙江省杭州市",
        "contact_email_label": "邮箱：",
        "contact_email_value": "export@greenleaf-demo.com",
        "contact_phone_label": "微信 / 电话：",
        "contact_phone_value": "+86-000-0000-0000",
        "contact_wechat_demo": "微信二维码（示意）：",
        "contact_footer_note": (
            "本网站为演示页面，用于展示茶叶及食品类出口品牌网站的可能呈现方式。"
        ),
        "contact_qr_alt": "微信二维码",

        # CONTACT FORM
        "form_name_label": "您的姓名",
        "form_name_placeholder": "请输入您的姓名",
        "form_company_label": "公司",
        "form_company_placeholder": "公司名称",
        "form_country_label": "国家 / 市场",
        "form_country_placeholder": "如：德国、阿联酋、美国",
        "form_email_label": "邮箱",
        "form_email_placeholder": "you@example.com",
        "form_message_label": "请简单介绍您的项目",
        "form_message_placeholder": "您的销售渠道、价格区间以及希望采购的茶类……",
        "form_submit": "发送询盘",
    },
}


def get_lang(default="en"):
    lang = request.args.get("lang", default)
    return "zh" if lang and lang.lower() in ("zh", "cn", "zh-cn") else "en"



@app.route("/")
def home():
    lang = get_lang()
    t = TEXTS[lang]
    return render_template("web2_tea_brand.html", t=t, lang=lang)


@app.route("/samples/factory")
def sample_factory():
    # keep old URL working, but redirect to main page with language
    lang = get_lang()
    return redirect(url_for("home", lang=lang))


if __name__ == "__main__":
    app.run(debug=True)
