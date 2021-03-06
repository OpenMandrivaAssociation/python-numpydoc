Name:           python-numpydoc
Version:	0.9.2
Release:	1
Summary:        Sphinx extension to support docstrings in Numpy format

License:        BSD
URL:            https://pypi.python.org/pypi/numpydoc
Source0:	https://files.pythonhosted.org/packages/b0/70/4d8c3f9f6783a57ac9cc7a076e5610c0cc4a96af543cafc9247ac307fbfe/numpydoc-0.9.2.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-sphinx

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose

%description
Numpydoc inserts a hook into Sphinx's autodoc that converts docstrings
following the Numpy/Scipy format to a form palatable to Sphinx.

%package -n python2-numpydoc
Summary:        Sphinx extension to support docstrings in Numpy format
%description -n python2-numpydoc
Numpydoc inserts a hook into Sphinx's autodoc that converts docstrings
following the Numpy/Scipy format to a form palatable to Sphinx.


%prep
%setup -q -n numpydoc-%{version}

rm -rf %{py3dir}
cp -a . %{py3dir}
2to3 --write --nobackups %{py3dir}

%build
%{__python2} setup.py build
pushd %{py3dir}
    %{__python3} setup.py build
popd


%install
pushd %{py3dir}
    %{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
    chmod -R a+r $RPM_BUILD_ROOT%{py3_puresitedir}/numpydoc-%{version}-py?.?.egg-info
popd
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
chmod -R a+r $RPM_BUILD_ROOT%{py2_puresitedir}/numpydoc-%{version}-py?.?.egg-info

%files
%doc LICENSE.txt
%{py_puresitedir}/numpydoc
%{py_puresitedir}/numpydoc-%{version}-py?.?.egg-info

%files -n python2-numpydoc
%doc LICENSE.txt
%{py2_puresitedir}/numpydoc
%{py2_puresitedir}/numpydoc-%{version}-py?.?.egg-info
