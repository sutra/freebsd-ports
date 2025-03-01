PORTNAME=	nsysctl
DISTVERSION=	2.1.1
CATEGORIES=	sysutils

MAINTAINER=	alfix86@gmail.com
COMMENT=	Utility to get and set kernel state at runtime
WWW=		https://gitlab.com/alfix/nsysctl/

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libsysctlmibinfo2.so:devel/libsysctlmibinfo2

USE_GITLAB=	yes

GL_ACCOUNT=	alfix
GL_COMMIT=	122f70b0c1556ee8d7862f532e62f8860c9dcce8

PLIST_FILES=	man/man8/${PORTNAME}.8.gz \
		sbin/${PORTNAME}
PORTDOCS=	CHANGELOG
PORTEXAMPLES=	file.conf

OPTIONS_DEFINE=	DOCS EXAMPLES

.include <bsd.port.pre.mk>

.if ${OPSYS} == FreeBSD && ${OSVERSION} >= 1400071
IGNORE=		uses struct sysctl_oid definition previous FreeBSD 1400071
.endif
.if ${OPSYS} != FreeBSD
IGNORE=		not supported on anything but FreeBSD
.endif

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/${PORTNAME} ${STAGEDIR}${PREFIX}/sbin
	${INSTALL_MAN} ${WRKSRC}/${PORTNAME}.8 ${STAGEDIR}${MAN8PREFIX}/man/man8/

do-install-DOCS-on:
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	${INSTALL_DATA} ${WRKSRC}/${PORTDOCS} ${STAGEDIR}${DOCSDIR}

do-install-EXAMPLES-on:
	@${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
	${INSTALL_DATA} ${WRKSRC}/${PORTEXAMPLES} ${STAGEDIR}${EXAMPLESDIR}

.include <bsd.port.post.mk>
