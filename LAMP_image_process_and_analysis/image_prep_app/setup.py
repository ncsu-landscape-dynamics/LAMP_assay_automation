from distutils import setup

setup(
    name='LAMP-assay-color-analysis-JAPOLO',
    version='0.1.0',
    author='John A. Polo',
    author_email='japolo@ncsu.edu',
    packages=['LAMP-assay-color-analysis'],
    scripts=[],
    url='https://github.com/ncsu-landscape-dynamics/LAMP_assay_automation',
    license='LICENSE',
    description='Image analysis resulting in color analysis of data from lab-on-a-chip.',
    long_description=open('README.md').read(),
    install_requires=[
	"numpy = "*"",
	"pillow="*"",
	"matplotlib="*"",
	"pandas="*"",
	"rawpy="*"",
	"torch="*"",
	"torchvision="*"",
	"opencv-python="*"",
	"pycocotools="*"",
	"gitpython="*"",
    ],
)