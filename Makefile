APK_VERSION := $(shell apk --version 2>/dev/null)
APT_VERSION := $(shell apt --version 2>/dev/null)
COMMAND=""

ifdef APK_VERSION
 OS_INSTALL=apk add

 OS_UNINSTALL=apk del

 OS_RUN_DEPS=python3  \
 			py2-pip \
			libsass

 OS_BUILD_DEPS=zlib-dev \
 			jpeg-dev \
			g++ \
			python3-dev

else ifdef APT_VERSION

 OS_INSTALL=sudo apt install -y 

 OS_UNINSTALL=sudo apt remove --auto-remove --purge -y 

 OS_RUN_DEPS=python3 \
 			python3-pip \
 			python3-libsass

 OS_BUILD_DEPS=

endif

PIP_INSTALL=pip3 install --upgrade 

PYTHON=python3

PIP_RUN_DEPS=django==2.2.1 \
			django-bootstrap-customizer \
			xhtml2pdf \
			django-crispy-forms \
			requests \
			unidecode \
			django_compressor \
			dj-static \
			kubernetes \
			whitenoise \
			sphinx \
			sphinx_materialdesign_theme

all: clean install update run

buildrun: build
		bash -c "firefox $(pwd)/build/doc/html/index.html &"
		bash -c "cd build/release && make run"

build: clean
		bash -c " \
			mkdir -p build &&\
			rsync -rv --exclude=build --exclude=.git . build &&\
			cd build &&\
			python3 setup.py build &&\
			sed -i 's;DEBUG = True;DEBUG = False;g' nuitdelinfo/settings.py &&\
			rm build -R &&\
			make html &&\
			mv build doc &&\
			mkdir release &&\
			mv * release || true &&\
			mv release/doc . "
		


install:
		@echo "########################## INSTALL DEPS #############################"

		@$(OS_UNINSTALL) $(OS_BUILD_DEPS)
		@$(OS_INSTALL) $(OS_RUN_DEPS)
		@$(OS_INSTALL) $(OS_BUILD_DEPS)
		@$(PIP_INSTALL) $(PIP_RUN_DEPS)
		@$(OS_UNINSTALL) $(OS_BUILD_DEPS)

		

clean: 
		@echo "########################## CLEAN #############################"
		@find . -path "*/migrations/*.py" -not -name "__init__.py" -delete 
		@find . -path "*/migrations/*.pyc" -delete 
		@find . -path "*/__pycache__/*.py" -not -name "__init__.py" -delete 
		@find . -path "*/__pycache__/*.pyc" -delete 
		@rm ./static/cache /tmp/django_cache ./build -R  || true


commit: clean 
		@echo "########################## COMMIT #############################"
		@git add . 
		@git commit



push: clean commit
		@echo "########################## PUSH #############################"
		@git push --all 


update: clean
		@echo "########################## UPDATE #############################"
		@rm database.db || true
		@$(PYTHON) manage.py makemigrations 
		@$(PYTHON) manage.py makemigrations --empty nuitdelinfo
		@$(PYTHON) manage.py makemigrations 
		@$(PYTHON) manage.py migrate  --run-syncdb 
		@echo "from django.contrib.auth import get_user_model;User = get_user_model();User.objects.create_superuser('adminsu', 'support@dotriver.eu', 'Shinu3G!');" | $(PYTHON) manage.py shell 


run:
		@$(PYTHON) manage.py runserver
		exit 0
		

ishell: clean 
		echo "$(COMMAND)" | $(PYTHON) manage.py shell
		
shell: clean 
	    $(PYTHON) manage.py shell
		

remoteupdate: 
		xfce4-terminal -e 'ssh -t root@10.255.0.248 ./update'



# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
