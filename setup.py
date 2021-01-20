import setuptools

setuptools.setup(
    name="GoodByeCorona",
    version="0.1",
    license='MIT',
    author="UniqueDevStorm",
    author_email="storm@uniquecode.team",
    description="굿바이코로나 Api를 가볍게 사용하기 위해 모듈로 제작하였습니다.",
    long_description=open('README.md').read(),
    url="https://github.com/UniqueDevStorm/GoodByeCorona",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)