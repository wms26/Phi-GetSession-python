# 萌新写的代码喵，可能不是很好喵，但是已经尽可能注释了喵，希望各位大佬谅解喵=v=
# ----------------------- 导包区 -----------------------
from os.path import (
    dirname,
    abspath,
    join,
    getsize,
)  # 对路径的一些操作以及获取文件大小
from subprocess import Popen, PIPE  # 运行adb指令用的
from json import loads  # 用来解析.userdata喵
from sys import argv  # 获取传入的参数喵

from logger import logger

# ---------------------- 定义赋值区 ----------------------

local_path = dirname(abspath(__file__))  # 获取当前脚本的绝对路径喵
# 将此模块绝对路径和adb路径拼接为adb的绝对路径喵，adb安卓调试桥的路径喵
adb_path = join(local_path, "adb\\adb.exe")
# 正确userdata大小的最小阈值喵(乘1024是因为os库获取到的以字节为单位喵)
userdata_minsize = 1 * 1024
userdata_name = ".userdata"  # userdata文件的文件名
userdata_path = f"/sdcard/Android/data/com.PigeonGames.Phigros/files/{userdata_name}"  # userdata在手机中的路径
userdata_out = join(local_path, ".userdata")  # userdata文件输出路径


def fuck_adb():
    runCmd(join(dirname(abspath(__file__)), "adb\\adb.exe") + " kill-server")


def runCmd(cmd: str, error_return: bool = False, print_error: bool = True):
    """
    运行cmd命令喵，可按需调整返回内容喵

    参数：
        cmd (str): 要运行的命令喵
        error_return (bool): 是否在错误流存在数据时只返回错误流数据喵
        print_error (bool): 是否打印错误到控制台喵

    返回：
        (str | None): 命令执行的结果
    """
    process = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)  # 运行命令喵
    out, err = process.communicate()  # 获取运行结果喵
    try:  # 先尝试使用utf-8解码喵(万恶的编码问题啊啊啊啊)
        output = out.decode("utf-8")
        error = err.decode("utf-8")

    except UnicodeDecodeError:  # 解码错误就换个编码再试喵
        output = out.decode("gbk")
        error = err.decode("gbk")

    if error != "":  # 如果错误不为空喵(不为空就是有错误喵)
        if print_error:
            logger.error("发生了错误喵：")
            logger.error(error)  # 输出错误信息喵

        if error_return:
            return error  # 返回错误以便进一步进行处理

        else:
            return None

    else:
        return output  # 没错误就输出执行结果喵


def adbCheck():
    """检查设备有没有正确连接adb"""
    runCmd(adb_path + " devices", print_error=False)
    output = runCmd(adb_path + " devices", error_return=True)

    # 判断关键字是否存在于输出内容中喵，不存在就证明没有连接adb喵
    if output is not None and "\tdevice" not in output:
        if "unauthorized" in output:
            raise Exception("你没有允许本计算机对手机进行调试喵！")

        elif "recovery" in output:
            raise Exception(
                "喵？你怎么在 Recovery 模式啊喵？请重启到系统先喵！"
            )

        else:
            raise Exception("没有任何设备连接到 adb 喵！")


def get_userdata():
    """使用adb获取phigros的.userdata"""
    logger.info("注意：获取 phigros 的 sessionToken需要先获取 .userdata 喵！")
    logger.info("注意：获取 .userdata 需要使用 adb 调试喵！")
    logger.info(
        '请先在手机上进入"开发者模式"喵！打开"USB调试"后用数据线将手机连接到电脑喵(平板也一样喵！)'
    )
    logger.info("如果在手机上弹出 USB 调试确认，请点击同意喵！")
    adbCheck()  # 检查adb是否正确连接
    logger.info(f'正在提取手机 Phigros 的 userdata，路径："{userdata_path}"')
    logger.info(runCmd(f"{adb_path} pull {userdata_path} {userdata_out}"))
    data_size = getsize(userdata_out)  # 获取提取出来的.userdata文件大小

    if data_size <= userdata_minsize:
        logger.error(
            f"获取到的 .userdata 大小不足 {userdata_minsize / 1024}KB 喵！仅有 {data_size / 1024}KB 喵！(共 {data_size} 字节喵)"
        )
        fuck_adb()
        logger.error("请再试几次，如果多次出现次错误请附带日志反馈喵！")
        raise ValueError

    logger.info(f'提取完成喵！路径喵："{userdata_out}"')
    return userdata_out


# ----------------------- 运行区 -----------------------

# 我也不知道为什么要留一个用来跳过提取userdata的参数喵(也许会有人用吧喵)
if len(argv) >= 2 and argv[1].lower() == "notget":
    userdata_path = "./.userdata"

elif len(argv) >= 2 and argv[1].lower() == "fuckadb":
    fuck_adb()  # 关掉adb
    exit()

else:
    # "企图"获取userdata喵，保存为.userdata文件喵
    userdata_path = get_userdata()
    fuck_adb()  # 关掉adb

with open(userdata_path, mode="r", encoding="utf-8") as file:  # 打开.userdata喵
    data = loads(file.read())  # 读取并解析.userdata喵
    # 输出sessionToken喵
    logger.info(f'你的sessionToken喵：{data["sessionToken"]}')
