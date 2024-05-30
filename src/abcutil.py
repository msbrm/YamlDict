import os
import re
import time


def get_now_str(format='%Y%m%d%H%M%S') -> str:
    return time.strftime(format)


def isTrue(obj):
    pass


def seconds2hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return int(hours), int(minutes), int(seconds)


def replace_env_variables(text):
    # 匹配 ${ENV_NAME} 形式的占位符
    pattern = re.compile(r'\$\{(\w+)\}')

    def replace_match(match):
        # 获取环境变量名称
        env_name = match.group(1)
        # 获取环境变量的值，默认空字符串
        return os.getenv(env_name, '')

    # 替换所有匹配的占位符
    return pattern.sub(replace_match, text)

    # # 示例字符串
    # example_text = "This is a path: ${HOME} and this is a user: ${USER}"

    # # 替换占位符
    # result = replace_env_variables(example_text)

    # print(result)


def replace_env_variables(text):
    # 使用非贪婪匹配模式
    pattern = re.compile(r'\$\{(\w+?)\}')

    def replace_match(match):
        # 获取环境变量名称
        env_name = match.group(1)
        # 获取环境变量的值，默认空字符串
        return os.getenv(env_name, '')

    # 替换所有匹配的占位符
    return pattern.sub(replace_match, text)

    # # 示例字符串包含多个占位符
    # example_text = "This is a path: ${HOME}, this is a user: ${USER}, and the shell is: ${SHELL}. Another path: ${PATH}."

    # # 替换占位符
    # result = replace_env_variables(example_text)

    # print(result)
