#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pytest_randomly
Version  : 3.15.0
Release  : 54
URL      : https://files.pythonhosted.org/packages/c9/d4/6e924a0b2855736d942703dec88dfc98b4fe0881c8fa849b6b0fbb9182fa/pytest_randomly-3.15.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c9/d4/6e924a0b2855736d942703dec88dfc98b4fe0881c8fa849b6b0fbb9182fa/pytest_randomly-3.15.0.tar.gz
Summary  : Pytest plugin to randomly order tests and control random.seed.
Group    : Development/Tools
License  : MIT
Requires: pypi-pytest_randomly-license = %{version}-%{release}
Requires: pypi-pytest_randomly-python = %{version}-%{release}
Requires: pypi-pytest_randomly-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
===============
pytest-randomly
===============
.. image:: https://img.shields.io/github/actions/workflow/status/pytest-dev/pytest-randomly/main.yml?branch=main&style=for-the-badge
:target: https://github.com/pytest-dev/pytest-randomly/actions?workflow=CI

%package license
Summary: license components for the pypi-pytest_randomly package.
Group: Default

%description license
license components for the pypi-pytest_randomly package.


%package python
Summary: python components for the pypi-pytest_randomly package.
Group: Default
Requires: pypi-pytest_randomly-python3 = %{version}-%{release}

%description python
python components for the pypi-pytest_randomly package.


%package python3
Summary: python3 components for the pypi-pytest_randomly package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_randomly)
Requires: pypi(pytest)

%description python3
python3 components for the pypi-pytest_randomly package.


%prep
%setup -q -n pytest_randomly-3.15.0
cd %{_builddir}/pytest_randomly-3.15.0
pushd ..
cp -a pytest_randomly-3.15.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692143735
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_randomly
cp %{_builddir}/pytest_randomly-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_randomly/99818029f54310d76088ea6f140f4d5ceb01c6b1 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytest_randomly/99818029f54310d76088ea6f140f4d5ceb01c6b1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
