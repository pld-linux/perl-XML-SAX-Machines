#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	SAX-Machines
%include	/usr/lib/rpm/macros.perl
Summary:	XML::SAX::Machines Perl module
Summary(cs.UTF-8):	Modul XML::SAX::Machines pro Perl
Summary(da.UTF-8):	Perlmodul XML::SAX::Machines
Summary(de.UTF-8):	XML::SAX::Machines Perl Modul
Summary(es.UTF-8):	Módulo de Perl XML::SAX::Machines
Summary(fr.UTF-8):	Module Perl XML::SAX::Machines
Summary(it.UTF-8):	Modulo di Perl XML::SAX::Machines
Summary(ja.UTF-8):	XML::SAX::Machines Perl モジュール
Summary(ko.UTF-8):	XML::SAX::Machines 펄 모줄
Summary(nb.UTF-8):	Perlmodul XML::SAX::Machines
Summary(pl.UTF-8):	Moduł Perla XML::SAX::Machines
Summary(pt.UTF-8):	Módulo de Perl XML::SAX::Machines
Summary(pt_BR.UTF-8):	Módulo Perl XML::SAX::Machines
Summary(ru.UTF-8):	Модуль для Perl XML::SAX::Machines
Summary(sv.UTF-8):	XML::SAX::Machines Perlmodul
Summary(uk.UTF-8):	Модуль для Perl XML::SAX::Machines
Summary(zh_CN.UTF-8):	XML::SAX::Machines Perl 模块
Name:		perl-XML-SAX-Machines
Version:	0.42
Release:	1
Epoch:		1
License:	Artistic, GPL or BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82cce7207bd50edd1d2386eea5e2c84b
URL:		http://search.cpan.org/dist/XML-SAX-Machines/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(XML::SAX::Base) >= 1.02
BuildRequires:	perl-XML-SAX >= 0.05
# doc say 0.4100001, so maybe too much, but safer
BuildRequires:	perl-XML-SAX-Writer >= 0.42
BuildRequires:	rpm-perlprov >= 4.1-13
%endif
Requires:	perl(XML::SAX::Base) >= 1.02
Requires:	perl-XML-SAX >= 0.05
# as above...
Requires:	perl-XML-SAX-Writer >= 0.42
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SAX::Machines is a collection of APIs that allow complex SAX
machines to be constructed without a huge amount of extra typing.

%description -l pl.UTF-8
XML::SAX::Machines to zestaw API pozwalający na konstruowanie
złożonych konstrukcji SAX bez dużej ilości nadmiarowego kodu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLSITELIB=$RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/XML/Filter/*.pm
%{perl_vendorlib}/XML/SAX/*.pm
%{perl_vendorlib}/XML/SAX/Machines
%{_mandir}/man3/*
