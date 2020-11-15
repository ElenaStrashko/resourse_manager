from setuptools import setup

setup(
	name='Resources_manager',
	version='1.0',
	py_modules=['Resources_manager', 'modules'],
	packages=['.', 'modules'],
	package_data={'modules/': ['*.py'], '.': ['*']},
	entry_points={
		'console_scripts': [
			'resources_manager = app:main',
		],
	},
)

