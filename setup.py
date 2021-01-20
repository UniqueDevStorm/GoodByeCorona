import setuptools

with open('./README.md', 'r', encoding='utf8') as f:
    md = f.read()

setuptools.setup(
    name="GoodByeCorona",
    version="1.0",
    license='MIT',
    author="UniqueDevStorm",
    author_email="storm@uniquecode.team",
    description="굿바이코로나 Api를 가볍게 사용하기 위해 모듈로 제작하였습니다.",
    long_description="""
    GoodByeCorona Api Module. 모든 저작권은 [굿바이코로나](https://corona-19.kr/) 에 있습니다.\n
    가볍게 디스코드 봇에 사용할수 있는 모듈을 만들었습니다. docs도 [굿바이코로나 Docs](https://github.com/dhlife09/Corona-19-API) 를 참고해주셨으면 합니다.\n
    사용하시려면 크레딧을 남겨주세요. ex) 모듈 : STORM#0001
    """,
    url="https://github.com/UniqueDevStorm/GoodByeCorona",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)