#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-notebook
Version  : 6.4.6
Release  : 81
URL      : https://files.pythonhosted.org/packages/3d/20/2dd607f13d12d7a8f10c4b4be53f76bcb2a0b76a431a127bce8d26442115/notebook-6.4.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/3d/20/2dd607f13d12d7a8f10c4b4be53f76bcb2a0b76a431a127bce8d26442115/notebook-6.4.6.tar.gz
Summary  : A web-based notebook environment for interactive computing
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: pypi-notebook-bin = %{version}-%{release}
Requires: pypi-notebook-data = %{version}-%{release}
Requires: pypi-notebook-license = %{version}-%{release}
Requires: pypi-notebook-python = %{version}-%{release}
Requires: pypi-notebook-python3 = %{version}-%{release}
Requires: Send2Trash
BuildRequires : buildreq-distutils3
Provides: notebook
Provides: notebook-python
Provides: notebook-python3
BuildRequires : pypi(jupyter_packaging)

%description
# Jupyter Notebook
[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Build Status](https://travis-ci.org/jupyter/notebook.svg?branch=master)](https://travis-ci.org/jupyter/notebook)
[![Documentation Status](https://readthedocs.org/projects/jupyter-notebook/badge/?version=latest)](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/jupyter/notebook/branch/master/graph/badge.svg)](https://codecov.io/gh/jupyter/notebook)

%package bin
Summary: bin components for the pypi-notebook package.
Group: Binaries
Requires: pypi-notebook-data = %{version}-%{release}
Requires: pypi-notebook-license = %{version}-%{release}

%description bin
bin components for the pypi-notebook package.


%package data
Summary: data components for the pypi-notebook package.
Group: Data

%description data
data components for the pypi-notebook package.


%package license
Summary: license components for the pypi-notebook package.
Group: Default

%description license
license components for the pypi-notebook package.


%package python
Summary: python components for the pypi-notebook package.
Group: Default
Requires: pypi-notebook-python3 = %{version}-%{release}

%description python
python components for the pypi-notebook package.


%package python3
Summary: python3 components for the pypi-notebook package.
Group: Default
Requires: python3-core
Provides: pypi(notebook)
Requires: pypi(argon2_cffi)
Requires: pypi(ipykernel)
Requires: pypi(ipython_genutils)
Requires: pypi(jinja2)
Requires: pypi(jupyter_client)
Requires: pypi(jupyter_core)
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
Requires: pypi(nest_asyncio)
Requires: pypi(prometheus_client)
Requires: pypi(pyzmq)
Requires: pypi(send2trash)
Requires: pypi(terminado)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-notebook package.


%prep
%setup -q -n notebook-6.4.6
cd %{_builddir}/notebook-6.4.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641459810
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-notebook
cp %{_builddir}/notebook-6.4.6/LICENSE %{buildroot}/usr/share/package-licenses/pypi-notebook/16d10493731a4bebeb353de88f3427006e13da11
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-bundlerextension
/usr/bin/jupyter-nbextension
/usr/bin/jupyter-notebook
/usr/bin/jupyter-serverextension

%files data
%defattr(-,root,root,-)
/usr/share/applications/jupyter-notebook.desktop
/usr/share/icons/hicolor/scalable/apps/notebook.svg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-notebook/16d10493731a4bebeb353de88f3427006e13da11

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
