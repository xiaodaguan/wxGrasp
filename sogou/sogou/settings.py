# -*- coding: utf-8 -*-

# Scrapy settings for sogou project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
LOG_LEVEL = 'INFO'
DOWNLOAD_DELAY = 5
RETRY_TIMES = 3
BOT_NAME = 'sogou'

SPIDER_MODULES = ['sogou.spiders']
NEWSPIDER_MODULE = 'sogou.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'sogou (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    # customize
    # 'sogou.middlewares.RandomProxy': 100,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

ITEM_PIPELINES = {
    'sogou.pipelines.SogouPipeline': 123,
}

PROXY_LIST = 'proxys.txt'
UA_LIST = 'uas.txt'
COOKIE_LIST = 'cookies.txt'

WEBDRIVER_USE_PROXY = False

REDIS_ADDRESS = "172.18.79.31:6379"
MONGODB_ADDRESS = "172.18.79.31:27017"
MONGODB_DB = "wechatdb"

WEBDRIVER_DELAY = "3-15" # seconds
MAX_PAGE = 10
MAX_RETRY = 3




SEARCH_KEYWORDS = [
        # '互联网金融 专家',
        # '网络借贷 专家',
        # '众筹融资 专家',
        # '互联网支付 专家',
        # '虚拟货币 专家',
        # '互联网基金 专家 ',
        # '互联网保险 专家',
        # '互联网消费金融 专家',
        # '互联网信托 专家',
        # '大数据金融 专家',
        # '互联网金融监管',
        # '互联网金融立法',
        # '互联网金融顶层设计',
        # '促进互联网金融健康发展指导意见',
        # '互联网金融指导意见',
        # '互联网金融基本法',
        # '互联网金融指南',
        # '互联网金融牌照',
        # '第三方支付牌照',
        # '互联网金融联盟',
        # '互联网金融行业协会',
        # '互联网金融分析报告',
        # '大数据金融分析报告',
        # '移动金融分析报告',
        # '互联网支付分析报告',
        # '网络借贷分析报告',
        # '众筹融资分析报告',
        # '虚拟货币分析报告',
        # '互联网金融公告',
        # '互联网信托公告',
        # '大数据金融公告',
        # '移动金融公告',
        # '互联网支付公告',
        # '网络借贷公告',
        # '众筹融资公告',
        # '互联网基金公告',
        # '互联网金融通报',
        # '互联网信托通报',
        # '大数据金融通报',
        # '移动金融通报',
        # '网络借贷通报',
        # '众筹融资通报',
        # '虚拟货币通报',
        # '互联网基金通报',
        # '互联网金融上市交易公告书',
        # '互联网信托上市交易公告书',
        # '移动金融上市交易公告书',
        # '互联网支付上市交易公告书',
        # '网络借贷上市交易公告书',
        # '众筹融资上市交易公告书',
        # '虚拟货币上市交易公告书',
        # '互联网基金上市交易公告书',
        # '互联网金融相关说明',
        # '大数据金融相关说明',
        # '移动金融相关说明',
        # '互联网支付相关说明',
        # '网络借贷相关说明',
        # '众筹融资相关说明',
        # '虚拟货币相关说明',
        # '互联网基金相关说明',
        # '质变',
        # '散户',
        # '逆袭',
        # '重庆城市通卡 金融',
        # '快付通 金融',
        # '医界贷 金融',
        # '友贷资本 金融',
        # '融贷通赢 金融',
        # '好贷网/心向优势 金融',
        # '国开行 金融',
        # '海秀网/北京海秀奥特科技 金融',
        # '万惠投融 金融',
        # '云中信Creditcloud 金融',
        # '瑞贷通 金融',
        # '智融财富 金融',
        # '宏信创投 金融',
        # '齐鲁证券 金融',
        # '青岛银行 金融',
        # '你我贷 金融',
        # '百付宝 金融',
        # '橙旗金融 金融',
        # '忧逸科技 金融',
        # '资信客 金融',
        # '吉信佳/壮壮贷款 金融',
        # '陕西易通商联 金融',
        # '超额宝 金融',
        # '易宝金融 金融',
        # '速贷邦 金融',
        # '360财富 金融',
        # '796交易所 金融',
        '拾财贷 金融',
        '银盒子 金融',
        '宜保通 金融',
        '百度 金融',
        '及时雨 金融',
        '惠人贷 金融',
        '天厚投资Tophold 金融',
        '在线贷 金融',
        '小企业E家 金融',
        '宝典创投 金融',
        '菠萝袋 金融',
        '大千 金融',
        '51贷/五一贷金融 金融',
        '赶牛网 金融',
        '复星集团 金融',
        '山东城联一卡通支付 金融',
        '乐融巴巴 金融',
        '融易融 金融',
        '东方支付 金融',
        '银盛支付 金融',
        '小雨伞保险 金融',
        '银视通 金融',
        '上海投融网 金融',
        '汇付数据 金融',
        '小铜人金融 金融',
        '湖北蓝天星 金融',
        '巴克莱银行 金融',
        'wPay微派支付 金融',
        '宁创贷 金融',
        '民民贷 金融',
        '365金融/世袭投资 金融',
        '慧银智能云POS 金融',
        '第三方机构支付',
        '互联网支付',
        '网络支付',
        '非金融机构支付',
        '移动支付',
        '第三方支付平台',
        '网银',
        '网上银行',
        '网络银行',
        '第三方辅助支付',
        '支付宝',
        '财付通',
        '银联商务',
        '快钱',
        '易宝',
        '拉卡拉',
        'PayPal',
        '微信支付',
        '二维码支付',
        '众筹',
        '网络众筹',
        '大众筹资',
        '群众集资',
        '众筹融资',
        '股权众筹',
        '债券众筹',
        '回报众筹',
        '捐赠众筹',
        '天使汇',
        'O2O众筹',
        '网络借贷',
        'P2P',
        'P2P信贷',
        '个人对个人',
        'P2P网络借贷',
        'P2P理财',
        '网贷',
        '网络贷款',
        '互联网小微金融',
        '网络小额贷款',
        '阿里金融',
        '资本市场',
        '股市',
        '十三五',
        '打黑',
        'Silvrr豆子科技 金融',
        '美冠信投 金融',
        '上海银商资讯 金融',
        '润通实业投资 金融',
        '齐鲁人贷 金融',
        '安徽皖垦商务 金融',
        '巾帼三六五 金融',
        '银讯网 金融',
        '财金汇/融信恒通 金融',
        '富途证券/富途牛牛 金融',
        '融金所 金融',
        'E微贷 金融',
        '蚂蚁金服 金融',
        '众筹第三方/稳利科技 金融',
        '分金社 金融',
        '先花花 金融',
        '金拐棍/财蕴天下 金融',
        '普蓝诺经济研究院 金融',
        '普天银通支付 金融',
        '上海魔卡 金融',
        '钱贷网 金融',
        '蚂蚁白领 金融',
        '借贷宝 金融',
        '新华传媒 金融',
        '闪白条 金融',
        '来客 金融',
        '山西易联数据处理 金融',
        '花哪了 金融',
        '中国银河证券 金融',
        '乐钱 金融',
        '好安贷 金融',
        '新工场投资 金融',
        '中钢银通 金融',
        '玺喜网(玺鉴金融) 金融',
        '阳光民间借贷 金融',
        '金电联行 金融',
        '呱呱贷 金融',
        '武汉城市一卡通 金融',
        '金融在线 金融',
        '91快车/衡惠金融 金融',
        '广亿贷 金融',
        '银库 金融',
        '聪头金融 金融',
        '银生宝支付 金融',
        '合创优贷 金融',
        '海绵保险-必保网络 金融',
        '广富宝 金融',
        '爱有财/零壹投资 金融',
        '钱升钱 金融',
        '有道金融 金融',
        '账贷通/联拓金融 金融',
        '亚术开发 金融',
        '壹卡会 金融',
        '蜀易贷 金融',
        '易八通/贝付科技 金融',
        '问投资 金融',
        '趣保科技/护驾 金融',
        '云付宝/万宝众合 金融',
        '比特币交易网 金融',
        '我爱众投 金融',
        '聚散贷 金融',
        'e生财富 金融',
        '平安银行 金融',
        '山东网上有名 金融',
        '国付宝 金融',
        '全球贷/环球财富 金融',
        '靠谱鸟 金融',
        '互利网 金融',
        '存折网 金融',
        '渝商创投 金融',
        '钱程网 金融',
        'my标客 金融',
        '搜钱网 金融',
        '瑞商贷 金融',
        '经钱网 金融',
        '信而富 金融',
        '湖南银河金谷 金融',
        '刷付通 金融',
        '晋商贷 金融',
        '真鑫贷 金融',
        '中民保险网 金融',
        '快汇宝 金融',
        '玖富咨询 金融',
        '石头理财 金融',
        '万象众筹 金融',
        '信通袋 金融',
        '移动金融',
        '移动银行',
        '移动支付',
        '掌上金融',
        '掌上银行',
        '手机银行',
        '手机支付',
        '移动证券',
        '移动保险',
        '微信支付',
        '移动端金融',
        '移动信贷',
        '马光远',
        '迁易通 金融',
        '众筹客 金融',
        '有利网 金融',
        '信互贷 金融',
        '美利金融 金融',
        '舟山明生商盟 金融',
        '融360 金融',
        '搜好贷 金融',
        '莱商贷 金融',
        '天天投/添砖加瓦 金融',
        '华悦财富 金融',
        '信用宝 金融',
        '天津金融资产交易所 金融',
        '账族网 金融',
        '泉州掌财通 金融',
        '中融财富 金融',
        '有人贷 金融',
        '京西创业投资 金融',
        '爱上理财 金融',
        '神州通付 金融',
        '翼龙贷 金融',
        '融易信 金融',
        '融华财富 金融',
        '合肥新思维 金融',
        '安贷客 金融',
        '煜隆创投 金融',
        '铜板街 金融',
        '中国电信 金融',
        '中金公司 金融',
        '六六投资 金融',
        '全民贷 金融',
        '微汇金融WeXFin 金融',
        '易通贷 金融',
        '保保18/保保网 金融',
        '新联在线 金融',
        '吉林省通卡支付股份 金融',
        '银豆网-债权交易网 金融',
        '商银信商业 金融',
        '财富说/财富达人网络 金融',
        '昆明卡互卡 金融',
        '币付宝 金融',
        '牛股王 金融',
        '凤凰金融 金融',
        '小商贷 金融',
        '爱投金融 金融',
        '财浪网 金融',
        '典阅科技 金融',
        '慧财网 金融',
        '华瑞富达 金融',
        '汇易宝 金融',
        '金融派/予墨信息 金融',
        '开联通 金融',
        '金e贷 金融',
        '工资钱包 金融',
        '富脑袋保险网 金融',
        '淘股吧 金融',
        '微贷网 金融',
        '空中贷 金融',
        '财付通 金融',
        '掌富网络 金融',
        '杭州惠借科技 金融',
        '光速创投 金融',
        '爱计算 金融',
        '樱桃派/九樱天下 金融',
        '银通贷/亿网银通 金融',
        '速帮贷 金融',
        '重庆千礼 金融',
        '浙江甬易支付 金融',
        'E速贷 金融',
        '通融易贷 金融',
        '汇瑞财富 金融',
        '闽昌贷 金融',
        '涌金贷 金融',
        '融易贷 金融',
        '众金在线 金融',
        '掌股专家 金融',
        '投资无忧/易八投资 金融',
        'TradingBot 金融',
        '金汇丰/汇诚创利 金融',
        '满满贷 金融',
        '钱袋网 金融',
        '资本魔方 金融',
        '华院数据 金融',
        '一城贷 金融',
        '众安保险 金融',
        '北京融易通 金融',
        '可信贷 金融',
        '钱贷贷 金融',
        '金蜗牛财富网 金融',
        '四达投资 金融',
        '联通支付 金融',
        '路演吧 金融',
        '8Securities 金融',
        '上海捷银支付 金融',
        '合盘贷 金融',
        '民生银行 金融',
        'OK车险/保橙网络 金融',
        '新外汇投资网ORTrader 金融',
        '易宝支付 金融',
        '展恒理财 金融',
        '口袋贵金属 金融',
        '天天基金 金融',
        '订单保/华甫达 金融',
        '烧饼猫 金融',
        '真融宝 金融',
        '富国数据 金融',
        '汇付宝 金融',
        '贝壳金服 金融',
        '山水聚宝 金融',
        '考拉理财 金融',
        '旺POS 金融',
        '河南贷 金融',
        '泰麟资本 金融',
        '贝米钱包 金融',
        '集利财富 金融',
        '好险啊 金融',
        '一起好 金融',
        'Gridseed 金融',
        '北京宽石量投 金融',
        '一贷网/上海微沙信息 金融',
        '好又贷 金融',
        'e融易贷 金融',
        '融信网 金融',
        '沃时贷 金融',
        '共鸣科技 金融',
        '深圳大明世纪 金融',
        '好贷网 金融',
        '聚财虎云记账 金融',
        '蜜蜂金服-蜂蜜理财 金融',
        '杉德 金融',
        '银联商务 金融',
        '摩根大通 金融',
        '抱财网 金融',
        '安心贷 金融',
        '爱投资/安投融 金融',
        '江苏旅通 金融',
        '高新盛 金融',
        '迅付 金融',
        '东方汇 金融',
        '睿信财富 金融',
        '民信贷 金融',
        '比特帮 金融',
        '友借友还/天道计然 金融',
        '融资城 金融',
        '方创APP-方创资本 金融',
        '徽商贷 金融',
        '贷齐乐 金融',
        '股360 金融',
        '商业高新技术发展 金融',
        '宜信财富 金融',
        '我爱创 金融',
        '我来操盘 金融',
        '集付通支付 金融',
        '广发基金 金融',
        '金贸街 金融',
        '互联网基金',
        '互联网+基金',
        '互联网金融基金',
        '互联网主题基金',
        '余额宝',
        '互联网金融指数',
        '在线理财',
        '互联网理财',
        '互联网保险',
        '互联网+保险',
        '云计算保险',
        '网络保险',
        '保险互联网化',
        '第三方保险',
        '互联网消费金融',
        '网络消费金融',
        '电商消费金融',
        '互联网分期购物',
        '消费金融',
        '分期乐',
        '优分期',
        '京东白条',
        '淘宝花呗',
        '小米贷款',
        '互联网消费信贷',
        '互联网信托',
        '网络信托',
        '互联网+信托',
        '互联网消费信托',
        '大数据金融',
        '大数据+金融',
        '大数据金融平台',
        '智能金融',
        '供应链金融',
        'SCF',
        '百度小贷',
        '百度金融',
        '阿里金融',
        '京东供应链金融',
        '苏宁供应链金融',
        '互联网+金融',
        '虚拟货币',
        '数字货币',
        '比特币',
        '旭日贷 金融',
        '比特金',
        '网络虚拟货币',
        '无限币',
        '夸克币',
        '神州易贷 金融',
        '大家投 金融',
        '慧保网 金融',
        '爱贝微支付 金融',
        '搜狐 金融',
        '三人贷 金融',
        'MEIX美市网 金融',
        '哈尔滨金联信 金融',
        '外汇助手 金融',
        '联正财富 金融',
        '国诚金融 金融',
        'Mybank迈伴客 金融',
        '和诚智达/运盈e贷 金融',
        '中诚信和支付 金融',
        '杭州捷蓝信息 金融',
        '连连银通支付 金融',
        '中国量化投资网 金融',
        '大连先锋 金融',
        '凤凰云科技/飞付卡 金融',
        '和信贷 金融',
        '卡卡理财 金融',
        '圈圈贷 金融',
        'Kivvi收银平板/瑞波电子/矽鼎科技 金融',
        '一起富 金融',
        '恒信通电信 金融',
        '银联商务 金融',
        '掌上贵金属/上海掌金信息 金融',
        '阿里巴巴 金融',
        '润京搜索投资 金融',
        'AngelCrunch 金融',
        '广西支付通 金融',
        '趣炒股/华赢科技 金融',
        '梦宝科技 金融',
        '天创信用 金融',
        '宽谷奥立安 金融',
        'DailyCost 金融',
        '易九金融 金融',
        '通联支付 金融',
        '草根投资网/草根网络 金融',
        '房金所 金融',
        '旺财谷 金融',
        '五十金50Jin 金融',
        '今日捷财 金融',
        '掌贝微POS(掌贝智能POS) 金融',
        '龙城易贷 金融',
        '爱钱进 金融',
        '银信联 金融',
        '融百科/上海沪谯金融 金融',
        'e融在线 金融',
        '邦帮堂 金融',
        '皖都金融 金融',
        '乐刷/移卡科技 金融',
        '腾讯 金融',
        '双乾服务 金融',
        '小赢理财 金融',
        '玖珑财富 金融',
        '京北金融-京北众筹 金融',
        '阿里路亚 金融',
        '国泰君安 金融',
        '币丰港/币丰支付 金融',
        '中汇在线 金融',
        '优优宝/五辰鑫达科技 金融',
        '盛典分期 金融',
        '趣分期 金融',
        '速溶360 金融',
        '厦门金利卡 金融',
        '有存网 金融',
        '融贝网 金融',
        '中汇支付 金融',
        '鑫隆创投 金融',
        '汇聚贷 金融',
        '很帅的投资客 金融',
        'Swipy红阳科技 金融',
        '南方基金 金融',
        '迪蒙科技 金融',
        '新疆润物 金融',
        '鑫银国际 金融',
        '金斧子 金融',
        'EMIE亿觅创意网 金融',
        '中筹网金 金融',
        '商旅通 金融',
        '3P银行 金融',
        '金评媒 金融',
        '数米基金网 金融',
        '汇金山/汇世软件 金融',
        '雪山贷 金融',
        '指财通/立佰趣 金融',
        '人人贷 金融',
        '车险无忧 金融',
        '筹趣网 金融',
        '微财/掌傲博科技 金融',
        '乐童音乐 金融',
        '真格贷/中融国金 金融',
        '人众金融 金融',
        '厦门夏商 金融',
        '91金融 金融',
        '花果金融 金融',
        '恒银金融科技 金融',
        '淘金路 金融',
        '票交网 金融',
        '华腾数据 金融',
        '盛付通支付 金融',
        'iShelly 金融',
        '好借好还 金融',
        '人人聚财 金融',
        '芥末金融 金融',
        '比特007 金融',
        '金融猪 金融',
        '安心de利/易融德利 金融',
        '76hui企乐汇/乐融多源 金融',
        '战国策 金融',
        '呼闪 金融',
        '资本在线 金融',
        '资本汇/乐投网络 金融',
        '希望金融 金融',
        '汉能 金融',
        '融卡科技 金融',
        '同城贷款 金融',
        '联合贷 金融',
        '众筹空间/轻众筹 金融',
        '理财魔方/口袋财富 金融',
        '天使客 金融',
        '雄猫软件 金融',
        '粒粒贷 金融',
        '汇通易贷 金融',
        '万维股票网 金融',
        '天翼电子商务 金融',
        '企e融-镭驰金控 金融',
        '网利金融 金融',
        '天风证券 金融',
        '天津荣程 金融',
        '投融界 金融',
        'WeLab我来贷 金融',
        '平平贷 金融',
        '杭州同盾科技 金融',
        '奇点集/奇点创投 金融',
        '网贷中国 金融',
        '惠金天下/上海裕能金融 金融',
        '乐易 金融',
        '普资华企 金融',
        '搜房网 金融',
        '巨和理财 金融',
        '保险岛 金融',
        'HelloMoney财富你好/芒柠网络 金融',
        '重庆市公众城市一卡通 金融',
        '乐投壹佰 金融',
        '口贷网 金融',
        '瑞银创投 金融',
        '汇潮支付 金融',
        '紫辰记账本 金融',
        '民生创投 金融',
        '聚云网络/深圳云娃科技/云付宝 金融',
        '广融贷 金融',
        '聚宝吧 金融',
        '玛瑙湾 金融',
        '什马金融 金融',
        '网信金融 金融',
        '宜信 金融',
        '瑞特商务 金融',
        '江苏鸿兴达邮政 金融',
        '量化派/量科邦 金融',
        '乐享易购享分期 金融',
        '摩点网/摩点众筹 金融',
        '财库网 金融',
        '德银 金融',
        '大通宝电子支付 金融',
        '爱卡贷 金融',
        '爱定投 金融',
        '汇通宝支付 金融',
        '金融一号店/投融有道 金融',
        '长沙商联 金融',
        '华夏商贷 金融',
        '诚信贷 金融',
        '优顾网 金融',
        '哆啦宝 金融',
        '好优贷 金融',
        '云理财/杭州千社科技 金融',
        '陕西邮政西邮寄 金融',
        '24Pay掌付通 金融',
        '百筹汇 金融',
        '前隆金融 金融',
        '繁星山谷 金融',
        '靠谱保 金融',
        '区块链',
        '银联支付',
        '群众募资',
        '天使投',
        'P2P金融',
        'P2P模式',
        '蚂蚁金服',
        '兴业银行 金融',
        '老虎证券 金融',
        '上海承泰信息/承泰无线移动传媒 金融',
        '北京梦哆啦网络 金融',
        '招财猫理财 金融',
        '贷小秘 金融',
        '易通支付 金融',
        '人人理财师 金融',
        '安徽瑞祥资讯 金融',
        '聚钱袋 金融',
        '湖南财信金通 金融',
        '拉手贷 金融',
        '小貔貅/朱赤禾木 金融',
        '稳收宝 金融',
        '专利众筹网 金融',
        '云币 金融',
        'Pad银行',
        '移动理财',
        '紫晶通财基金 金融',
        '华生贷 金融',
        '山东省电子商务综合运营 金融',
        '融贷通 金融',
        '绿能宝 金融',
        '易贷网 金融',
        '商联信支付 金融',
        '春华资本集团 金融',
        '热贷网/上海百银金融 金融',
        '众信金融 金融',
        '福建国通星驿 金融',
        '数字王府井 金融',
        '米牛网 金融',
        '爱交子 金融',
        '工行 金融',
        '信托网 金融',
        '紫枫信贷 金融',
        '安徽圣德天开 金融',
        '锦江国际 金融',
        '友友贷 金融',
        '盛融在线 金融',
        '日益创投 金融',
        '成都易分期 金融',
        'Formax福亿 金融',
        '51分期网 金融',
        '三维度商城 金融',
        '好帮贷 金融',
        '北京新浪互联信息服务有限公司 金融',
        '智慧金融',
        '阿里小贷',
        '互联网金融',
        '莱特货币',
        '泽塔币',
        '寰融信息GFT 金融',
        '司马钱 金融',
        '财豹 金融',
        '友股网 金融',
        '人人聚财 金融',
        '金海贷 金融',
        '易融恒信 金融',
        '乐贷通 金融',
        '联和金融 金融',
        '上海航运运价交易SSEFC 金融',
        '心跳投资 金融',
        '多钱网 金融',
        '融道网 金融',
        '和融通 金融',
        'Mo宝/成都摩宝 金融',
        '金信网 金融',
        '联亿家 金融',
        '广东嘉联支付 金融',
        'CreditBit信用币 金融',
        '汇明 金融',
        '速可贷 金融',
        '九次方大数据 金融',
        '简单理财网 金融',
        '成都财智软件 金融',
        '投哪网 金融',
        '财经道/衡怡智能 金融',
        '郑州建业至尊 金融',
        '中百支付 金融',
        '浙江快捷通 金融',
        '鹰皇金佰仕 金融',
        '钜派投资 金融',
        '花生米支付 金融',
        '弘昌创投 金融',
        '考拉征信 金融',
        '百融金服 金融',
        '闪电借款 金融',
        '中信银行 金融',
        '云财经/珠海富讯网络 金融',
        '银客网 金融',
        '锐博汇通 金融',
        '聚测无忧 金融',
        '美家付 金融',
        '交通银行 金融',
        '福建一卡通 金融',
        'BtcTrade比特币交易网 金融',
        '玖那里/那里贷 金融',
        '和君咨询 金融',
        '莴苣账本 金融',
        '桔子理财 金融',
        '易融贷 金融',
        '有人贷/安信卓越 金融',
        '多盈网 金融',
        '银票网 金融',
        '搜富580 金融',
        '高汇通 金融',
        '诚意贷 金融',
        '付费通 金融',
        '邦融理财 金融',
        '爱贷网 金融',
        '大钱信息 金融',
        '微贷中国 金融',
        '觉JUE.SO 金融',
        '徽州贷 金融',
        '卡宝宝网 金融',
        'PPmoney 金融',
        '微金所 金融',
        '红岭创投 金融',
        '产融贷 金融',
        '和盛在线 金融',
        '朋友范 金融',
        '交广发展 金融',
        '超交易 金融',
        '99无限/上海瀚银 金融',
        '第一P2P/网信金融 金融',
        '搜贷网 金融',
        '路人甲/汇涓时代 金融',
        '易投理财 金融',
        'PosPal银豹收银系统 金融',
        '互联行 金融',
        '中国邮政储蓄银行 金融',
        '火球网/北京玄铁科技 金融',
        '汇元银通 金融',
        '招商基金 金融',
        '信融财富 金融',
        '天使汇 金融',
        '标准众筹 金融',
        '租房宝 金融',
        '金诚通支付 金融',
        '易网贷 金融',
        '贝贝贷 金融',
        '引力波',
        '人机围棋',
        '普惠金融信息服务公司',
        '放心保 金融',
        '大融小贷 金融',
        '南京万商 金融',
        '91贷款网 金融',
        '玖融网 金融',
        '金融圈 金融',
        '山西金虎 金融',
        '中科柏诚科技 金融',
        '投资脉搏 金融',
        '信客网 金融',
        '丰投网 金融',
        '和堂金融 金融',
        '挖财 金融',
        '微金互助 金融',
        '联帮贷 金融',
        '好项目 金融',
        '东方睿赢 金融',
        '汇通达 金融',
        '百财车贷 金融',
        '八条鱼 金融',
        '意时网 金融',
        '普天贷 金融',
        '天天盈/汇付天下 金融',
        '上海诚数信息技术有限公司 金融',
        '乐融网 金融',
        '佳盟金融网 金融',
        '中青创投网 金融',
        'e家保险网/亿保网络 金融',
        '淘贷宝 金融',
        '全诚在线 金融',
        '联信财富 金融',
        '汇贷中国网 金融',
        '小财神 金融',
        '巨涟金融 金融',
        '熟信 金融',
        '万通财富 金融',
        '瑞得 金融',
        '云南银通 金融',
        '温商贷 金融',
        '摇钱树 金融',
        '星理财 金融',
        '多多财富网 金融',
        '中汇金电子商务 金融',
        '火币网 金融',
        '畅贷网 金融',
        '金融港/滚雪球财富 金融',
        '贷帮网 金融',
        '融易投 金融',
        '扑满Puman 金融',
        '海南新生 金融',
        '网贷之家 金融',
        '壹财富/小虎金融 金融',
        '爱钱帮 金融',
        '中国人保财险 金融',
        '分期乐 金融',
        '兆尹科技 金融',
        '上海证券 金融',
        '诺诺镑客NonoBank 金融',
        '钱包金服 金融',
        '中付支付 金融',
        '淘梦网 金融',
        '无锡市民卡 金融',
        '移动账金融 专家',
        '互联网金融规范',
        '互联网信托分析报告',
        '互联网基金分析报告',
        '虚拟货币公告',
        '互联网支付通报',
        '大数据金融上市交易公告书',
        '互联网信托相关说明',
        'A股',
        '维信理财 金融',
        '快速贷 金融',
        '资和信通联 金融',
        '借点儿 金融',
        '洋钱罐 金融',
        '深圳华营数字 金融',
        '汇添富 金融',
        '宜人贷 金融',
        'OKcoin比特币 金融',
        '微财网/大简信息 金融',
        '99分期/好斌金融 金融',
        '中宝投资 金融',
        '手机支付',
        '手机银行',
        '汇付天下',
        '汇众财富 金融',
        '顺付卡 金融',
        '艺商贷 金融',
        '夸客金融 金融',
        '恩牛网络 金融',
        '阜鼎保理/阜鼎汇通商业保理 金融',
        'BBD数联铭品 金融',
        '江西缴费通 金融',
        '重庆贷 金融',
        '商富贷 金融',
        '中天嘉华 金融',
        '百付天下/上海翰鑫 金融',
        '财帮子 金融',
        '和诚德在线 金融',
        '点石微投行 金融',
        '中贸易融 金融',
        '义乌贷 金融',
        '点点贷 金融',
        '91征信 金融',
        '穗金所 金融',
        '信贷宝 金融',
        '金鲤鱼短理/尚世同禾 金融',
        '天津积木 金融',
        '众筹空间 金融',
        '铜掌柜 金融',
        '恒达万华商业经纪 金融',
        '热贷网 金融',
        '雪球财经 金融',
        '股票管家 金融',
        '忙乐网 金融',
        '富途网/富途证券 金融',
        '金掌柜/汇卡商务 金融',
        '五洲财富 金融',
        '送姜很行 金融',
        '点火网 金融',
        '年享财富 金融',
        '向上360/证大向上网络 金融',
        '工付宝 金融',
        '徽融通 金融',
        '365易贷 金融',
        '大乔易贷 金融',
        '西安银信商通 金融',
        '车爱保 金融',
        '融和友信 金融',
        '极光账本 金融',
        '炒饭 金融',
        '浙江商贷 金融',
        '国佳财富 金融',
        '润客投资 金融',
        '新新贷 金融',
        '证大e贷 金融',
        '好买基金网/好买财富 金融',
        '开心贷 金融',
        '融易贷 金融',
        '温州二手车商城网 金融',
        '票据客/富商金融 金融',
        '未来研究所 金融',
        '大特保 金融',
        '48Hourslogo 金融',
        '银通贷 金融',
        '浙江航天电子信息产业 金融',
        '艺恩汇 金融',
        '小股神/北京乐不思蜀科技 金融',
        '财商通 金融',
        '恒富在线 金融',
        '华夏通宝 金融',
        '大麦理财 金融',
        '合力贷 金融',
        '钱爸爸网贷 金融',
        '德圣基金研究中心 金融',
        'P2P圈 金融',
        '爱钱包 金融',
        '仁仁分期 金融',
        '融融网 金融',
        '河北御嘉 金融',
        '黄金钱包 金融',
        '钱多多/旭胜金融 金融',
        '银通支付 金融',
        '乐投天下 金融',
        '地标金融 金融',
        '警安财富 金融',
        '贷帮 金融',
        '合拍在线 金融',
        '农分期-种子金服 金融',
        '51金服-网贷工场 金融',
        '盒子支付 金融',
        '易筹网/方丁易筹 金融',
        '联投网 金融',
        '优分期/和创未来 金融',
        '365金融 金融',
        '随手科技 金融',
        '一路财富 金融',
        '豫商贷/豫商贷网络 金融',
        '鼎力投资网 金融',
        '广信贷 金融',
        '陆金所 金融',
        'PingPlusPlus拼谱啦 金融',
        '普惠贷 金融',
        '聚爱财 金融',
        'RockMiner 金融',
        '钱先生 金融',
        '湖南星广传媒 金融',
        '力天财经网 金融',
        '盼贷网 金融',
        '安徽长润支付 金融',
        '音付/斯寄乐SGL 金融',
        '草根新贷 金融',
        '诺诺镑客 金融',
        '会生活/随行付 金融',
        '她理财 金融',
        '卡友支付 金融',
        '宽客网 金融',
        '北京邮政 金融',
        '金蝶金链 金融',
        '苏宁云商 金融',
        '融金汇银 金融',
        '通卡投资 金融',
        '网融天下 金融',
        '公明贷 金融',
        '深圳商贷 金融',
        '磁金融 金融',
        '聚财村 金融',
        '互联网金融千人会 金融',
        '恒信易贷 金融',
        '盛世创投 金融',
        '寻钱网 金融',
        '投投是道 金融',
        '随时融 金融',
        '易融网 金融',
        '米多财富 金融',
        '维金Vfinance 金融',
        '808信贷 金融',
        '东方融资网 金融',
        '山西兰花大酒店 金融',
        '京金联 金融',
        '掌上汇通 金融',
        '短融网 金融',
        '云贷网 金融',
        '工商贷 金融',
        'VCHello微投网 金融',
        '网银在线 金融',
        '南京苏宁易付宝 金融',
        '信和贷 金融',
        '雅酷时空 金融',
        '鲁商贷 金融',
        '追梦网 金融',
        '甬商贷 金融',
        '中国人民银行金融研究所 金融',
        '彩云BANK-聚识金融 金融',
        '开开贷 金融',
        '宜信基金/宜信普泽 金融',
        '中金在线 金融',
        '即科金融Geex Finance 金融',
        '天弘基金 金融',
        '中国梦网 金融',
        '微付 金融',
        '拉卡拉 金融',
        '光大银行 金融',
        '天金加银 金融',
        '钱袋宝 金融',
        '呼哧旅行支票/麦信卓越科技 金融',
        '海色网 金融',
        '云信汇通 金融',
        '员工宝/诺亚易捷金融 金融',
        '保本无忧 金融',
        '商联商用 金融',
        '佰易贷 金融',
        '发展投资 金融',
        '必投宝 金融',
        '礼德财富 金融',
        '麦子金服 金融',
        '君融贷 金融',
        '好想贷 金融',
        'Wecash 闪银 金融',
        '国旅 金融',
        '优股网/优股雷达 金融',
        '互贷网 金融',
        '江苏爱心消费支付 金融',
        '财人汇 金融',
        '合道融通/合融网 金融',
        '小蚁BitAngelsClub 金融',
        '移联支付/随意刷 金融',
        '哈哈贷 金融',
        '联拓金融 金融',
        '上海瀚银科技/手付通 金融',
        '江苏金禧智能卡 金融',
        'e乐充 金融',
        'RippleCN锐博汇通科技 金融',
        '共赢社/深圳中融资本 金融',
        '点心贷/点心科技 金融',
        '金豪利 金融',
        '幸福e贷 金融',
        '豫商贷 金融',
        '金融堂 金融',
        '诚汇通 金融',
        '爱保网 金融',
        '浙江银付通 金融',
        '有钱贷 金融',
        '通付盾 金融',
        'WeLend 金融',
        '爱学贷 金融',
        '钱海 金融',
        '19pay一九付/高阳捷迅 金融',
        '德弘资产 金融',
        '广州银联支付 金融',
        '融金通 金融',
        '团贷网 金融',
        '基金豆 金融',
        '恒生电子 金融',
        '爱互融 金融',
        '爱投资 金融',
        '全民财富/上海欣亨金融 金融',
        '理财宝宝网 金融',
        '起点贷 金融',
        'Kaistart开始众筹 金融',
        '兴业证券 金融',
        '锦融运通 金融',
        '积木盒子 金融',
        '电网贷 金融',
        '第一网贷 金融',
        '湖湘贷 金融',
        '广融在线 金融',
        '永利宝金融 金融',
        '轻纺城金融 金融',
        '三信贷 金融',
        '商银 金融',
        '24财富 金融',
        '中币交易所 金融',
        '卡友汇 金融',
        '铂利亚 金融',
        '紫桐金融 金融',
        '小牛网 金融',
        '幸福贷 金融',
        '小福记账理财 金融',
        '招商贷 金融',
        '优势财富-U 优财 金融',
        '创投圈 金融',
        '恒丰财富 金融',
        '京东金融 金融',
        '贷贷网 金融',
        '宝点网 金融',
        'e云贷 金融',
        '银博盛世 金融',
        '易宝支付 金融',
        'Wisdom维氏盾-易起查 金融',
        '富友支付/随心富 金融',
        '卡小二 金融',
        '未来付网络 金融',
        '积储在线 金融',
        '银联支付 金融',
        '瑞波币中国/XRP China 金融',
        '易界网/DealGlobe 金融',
        '开心保 金融',
        '明亚保险 金融',
        '贷得快 金融',
        '温州贷 金融',
        '点融网 金融',
        '安付宝商务 金融',
        '盈盈理财 金融',
        '财鱼管家 金融',
        '钱小二 金融',
        '比特币中国/上海萨图西网络 金融',
        '专投网 金融',
        '华尔街见闻 金融',
        '创艺网 金融',
        '车能贷 金融',
        'AutoFLY小额贷款网 金融',
        '多牛网 金融',
        '融时代 金融',
        '大大财经 金融',
        '高搜易 金融',
        '成都天府通金融 金融',
        '马展金融 金融',
        '正能贷 金融',
        '最操盘 金融',
        '优保网 金融',
        'ChinaScope数库 金融',
        '神州融/神州微融 金融',
        '币行/友聚惠 金融',
        '亿付数字 金融',
        '安硕信息Amarsoft 金融',
        '大童网 金融',
        '万家兄弟 金融',
        '快钱支付 金融',
        '融信优贝/联通华建 金融',
        '51理财 金融',
        '美贷网 金融',
        '杭州市民卡 金融',
        '丁丁贷 金融',
        '在线贷/鼎丰在线 金融',
        '你我贷/嘉银金融 金融',
        '安徽省万事通金卡通 金融',
        '江苏省中心 金融',
        '保险e超市/亿保网络 金融',
        '国金证券 金融',
        '推理财/江海科技JHM 金融',
        '钱大人 金融',
        '阿思拓 金融',
        '交易家 金融',
        '东方汇融 金融',
        '融信财富 金融',
        '中投 金融',
        '集优贷 金融',
        '平安集团 金融',
        '宏源证券 金融',
        '赚赚金融 金融',
        '财报狗 金融',
        '农商贷 金融',
        '信托100/财商通 金融',
        '懒投资/大家玩 金融',
        '乾贷网 金融',
        '恒银金融 金融',
        '中纳联投 金融',
        '千牛网 金融',
        '小鹅e贷 金融',
        '数银在线 金融',
        '众人贷 金融',
        '资产360 金融',
        '微美贷VMdai 金融',
        '兄弟高登 金融',
        '拍拍贷 金融',
        '云筹网 金融',
        '好利贷 金融',
        '信诚贷 金融',
        '票据宝 金融',
        '迅贷 金融',
        '瑞银证券 金融',
        '德邦基金 金融',
        '紫金贷 金融',
        '开鑫贷 金融',
        '优乐股份 金融',
        '支付宝 金融',
        '沐金农 金融',
        '融众网 金融',
        '安徽华夏通支付 金融',
        '麦圈活动 金融',
        '付融宝 金融',
        '钱景财富 金融',
        '掌贷宝/融都科技 金融',
        '上海屹通信息 金融',
        '酷贷网 金融',
        '飞速贷 金融',
        '合时代 金融',
        '鑫合汇 金融',
        '招行 金融',
        '众投邦 金融',
        '微金互助网 金融',
        '大数金融 金融',
        '帮客创投 金融',
        '向日葵保险网 金融',
        '国临创投 金融',
        '思创银联 金融',
        '理财超市/乐财 金融',
        '杭州盛炬 金融',
        '中信贷 金融',
        '丰达财富 金融',
        '财来网 金融',
        '上海讯联数据 金融',
        '私银家-友道财富 金融',
        '大众卡惠 金融',
        '蚂蚁微股 金融',
        '合盈网贷 金融',
        '证联融通电子 金融',
        '华北贷 金融',
        'MoneyCoin/暘碁资讯 金融',
        '诺瓦金融信息 金融',
        '大家保 金融',
        '玖玖金融 金融',
        '惠众金融 金融',
        '酷皮 金融',
        '裕福支付 金融',
        '开财宝 金融',
        '亿金融 金融',
        '艾德睿智 金融',
        '钱方 金融',
        '赢众投 金融',
        '懒财网 金融',
        '人人操盘 金融',
        '点名时间 金融'
    ]