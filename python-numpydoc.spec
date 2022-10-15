Name:           python-numpydoc
Version:	1.5.0
Release:	1
Summary:        Sphinx extension to support docstrings in Numpy format

License:        BSD
URL:            https://pypi.python.org/pypi/numpydoc
Source0:	https://files.pythonhosted.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-sphinx

%description
Numpydoc inserts a hook into Sphinx's autodoc that converts docstrings
following the Numpy/Scipy format to a form palatable to Sphinx.

%prep
%autosetup -p1 -n numpydoc-%{version}

%build
%py_build

%install
%py_install
chmod -R a+r $RPM_BUILD_ROOT%{py3_puresitedir}/numpydoc-%{version}-py*.egg-info

%files
%doc LICENSE.txt
%{py_puresitedir}/numpydoc
%{py_puresitedir}/numpydoc-%{version}-py*.egg-info
