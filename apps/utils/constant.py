# 模型
AI_IS_USED = (
    (0, "使用异常"),
    (1, "未使用"),
    (2, "使用中"),
)

AI_SOURCE = (
    (0, "手动添加"),
    (1, "平台导入"),
)

# 设备
D_STATUS = ((0, "离线"), (1, "在线"), (2, "异常"))

D_TYPE = ((0, "智能摄像机"), (1, "网络摄像机"))

D_SOURCE = (
    (0, "手动添加"),
    (1, "平台导入"),
)

D_BRAND = (
    (0, "海康"),
    (1, "大华"),
    (2, "华为"),
    (3, "宇视"),
    (4, "未知"),
    (5, "自定义"),
)

D_FORMAT = (
    (0, "RTSP"),
    (1, "ONVIF"),
    (2, "GB28181"),
    (3, "GAT1400"),
)

S_CONFIG = (
    (0, "人脸/车牌图"),
    (1, "行人/机动车/非机动车图"),
    (2, "全景图"),
)