#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	WordFind
Summary:	Games::WordFind Perl module
Summary(cs):	Modul Games::WordFind pro Perl
Summary(da):	Perlmodul Games::WordFind
Summary(de):	Games::WordFind Perl Modul
Summary(es):	M�dulo de Perl Games::WordFind
Summary(fr):	Module Perl Games::WordFind
Summary(it):	Modulo di Perl Games::WordFind
Summary(ja):	Games::WordFind Perl �⥸�塼��
Summary(ko):	Games::WordFind �� ����
Summary(no):	Perlmodul Games::WordFind
Summary(pl):	Modu� Perla Games::WordFind
Summary(pt):	M�dulo de Perl Games::WordFind
Summary(pt_BR):	M�dulo Perl Games::WordFind
Summary(ru):	������ ��� Perl Games::WordFind
Summary(sv):	Games::WordFind Perlmodul
Summary(uk):	������ ��� Perl Games::WordFind
Summary(zh_CN):	Games::WordFind Perl ģ��
Name:		perl-Games-WordFind
Version:	0.02
Release:	13
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	28bfa49532f2a49fd455fbd3b9afeb9e
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games::WordFind module simply provides a class which can be used to
generate WordFind type puzzles.

%description -l pl
Games::WordFind udost�pnia klas� do generowania uk�adanek s�ownych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Games/WordFind.pm
%dir %{perl_vendorlib}/auto/Games
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/Games/WordFind
#%%{perl_vendorlib}/auto/Games/WordFind/autosplit.ix
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*