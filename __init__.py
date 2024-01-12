import pyautogui
import comfy
import comfy.utils

from .screenshots import Screenshots
from .groupBypassCn import BypassGroupControlNode


# 设置每个节点的CATEGORY属性确保它们在UI中被归类到"Blueraincoat"组
Screenshots.CATEGORY = "Blueraincoat"
BypassGroupControlNode.CATEGORY = "Blueraincoat"


NODE_CLASS_MAPPINGS = {
    "Screenshots": Screenshots,
    "BypassGroupControlNode": BypassGroupControlNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Screenshots": "Screen Shots",
    "BypassGroupControlNode": "Bypass Group Control Node",
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]
