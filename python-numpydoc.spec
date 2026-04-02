%define module numpydoc

Name:		python-numpydoc
Summary:	Sphinx extension to support docstrings in Numpy format
Version:	1.10.0
Release:	1
License:	BSD-2-Clause
URL:		https://pypi.python.org/pypi/numpydoc
Source0:	https://files.pythonhosted.org/packages/source/n/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(sphinx)

%description
%{name}} provides the numpydoc Sphinx extension for handling docstrings
formatted according to the NumPy documentation format.

The extension also adds the code description directives:
np:function, np-c:function, etc.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc LICENSE.txt
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
