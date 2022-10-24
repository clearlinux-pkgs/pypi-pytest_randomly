#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytest_randomly
Version  : 3.12.0
Release  : 49
URL      : https://files.pythonhosted.org/packages/2e/1c/35f9746b7bd794e205f3a70ae0d6e167d2c929342e15de40d9d37f3b675e/pytest-randomly-3.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/1c/35f9746b7bd794e205f3a70ae0d6e167d2c929342e15de40d9d37f3b675e/pytest-randomly-3.12.0.tar.gz
Summary  : Pytest plugin to randomly order tests and control random.seed.
Group    : Development/Tools
License  : MIT
Requires: pypi-pytest_randomly-license = %{version}-%{release}
Requires: pypi-pytest_randomly-python = %{version}-%{release}
Requires: pypi-pytest_randomly-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pytest)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
===============
pytest-randomly
===============
.. image:: https://img.shields.io/github/workflow/status/pytest-dev/pytest-randomly/CI/main?style=for-the-badge
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
%setup -q -n pytest-randomly-3.12.0
cd %{_builddir}/pytest-randomly-3.12.0
pushd ..
cp -a pytest-randomly-3.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656401035
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_randomly
cp %{_builddir}/pytest-randomly-3.12.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_randomly/99818029f54310d76088ea6f140f4d5ceb01c6b1
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
