#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define		pdir	IP
%define		pnam	Country-DB_File
Summary:	IP::Country::DB_File - IPv4 and IPv6 to country translation using DB_File
Name:		perl-IP-Country-DB_File
Version:	3.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	749ea4ca65126ef38d30bb386865c49e
URL:		https://metacpan.org/dist/IP-Country-DB_File
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Math-Int64
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IP::Country::DB_File is a light-weight module for fast IP address to
country translation based on DB_File. The country code database is
stored in a Berkeley DB file. You have to build the database using
build_ipcc.pl or IP::Country::DB_File::Builder before you can lookup
country codes.

This module tries to be API compatible with the other IP::Country
modules. The installation of IP::Country is not required.

There are many other modules for locating IP addresses. Neil Bowers
posted an excellent review. Some features that make this module
unique:

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/build_ipcc.pl
%{perl_vendorlib}/IP/Country/*.pm
%{perl_vendorlib}/IP/Country/DB_File
%{_mandir}/man1/build_ipcc.pl.1*
%{_mandir}/man3/IP::Country::DB_File*.3*
