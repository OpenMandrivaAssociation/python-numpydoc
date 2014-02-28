# Disabled for now untill a new release will be on pypi with these patches:
# https://github.com/numpy/numpy/pull/2994
%global with_python3 0


Name:           python-numpydoc
Version:        0.4
Release:        2%{?dist}
Summary:        Sphinx extension to support docstrings in Numpy format

License:        BSD
URL:            https://pypi.python.org/pypi/numpydoc
Source0:        https://pypi.python.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-nose
BuildRequires:  python-sphinx
BuildRequires:  python-matplotlib

%if 0%{with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-sphinx
BuildRequires:  python3-matplotlib
BuildRequires:  python2-tools
%endif

%description
Numpydoc inserts a hook into Sphinx's autodoc that converts docstrings
following the Numpy/Scipy format to a form palatable to Sphinx.

%if 0%{with_python3}
%package -n python3-numpydoc
Summary:        Sphinx extension to support docstrings in Numpy format
%description -n python3-numpydoc
Numpydoc inserts a hook into Sphinx's autodoc that converts docstrings
following the Numpy/Scipy format to a form palatable to Sphinx.
%endif


%prep
%setup -q -n numpydoc-%{version}

%if %{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
2to3 --write --nobackups %{py3dir}
sed -i "s/\.docscrape/docscrape/g" %{py3dir}/docscrape_sphinx.py
%endif


%build
%{__python} setup.py build
%if %{?with_python3}
pushd %{py3dir}
    %{__python3} setup.py build
popd
%endif


%install
%if %{?with_python3}
pushd %{py3dir}
    %{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%check
nosetests -v
%if 0%{with_python3}
pushd %{py3dir}
    %{_bindir}/nosetests-3* -v || :
popd
%endif

 
%files
%doc LICENSE.txt
%{_bindir}/autosummary_generate
%{python_sitelib}/numpydoc
%{python_sitelib}/numpydoc-%{version}-py?.?.egg-info

%if 0%{with_python3}
%files -n python3-numpydoc
%doc LICENSE.txt
%{_bindir}/autosummary_generate
%{python3_sitelib}/numpydoc
%{python3_sitelib}/numpydoc-%{version}-py?.?.egg-info
%endif

%changelog
* Mon Aug  5 2013 Thomas Spura <tomspur@fedoraproject.org> - 0.4-2
- BR python2-devel, python-sphinx, python-nose
- use macro in URL
- disable python3 package for now

* Fri Aug  2 2013 Thomas Spura <tomspur@fedoraproject.org> - 0.4-1
- initial package
