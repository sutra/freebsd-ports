PORTNAME=	packer
PORTVERSION=	1.7.10
DISTVERSIONPREFIX=	v
PORTREVISION=	6
CATEGORIES=	sysutils

MAINTAINER=	brad@facefault.org
COMMENT=	Tool for creating machine images
WWW=		https://packer.io/

LICENSE=	MPL20
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		cpe go:modules
CPE_VENDOR=	hashicorp
GO_MODULE=	github.com/hashicorp/packer

PLIST_FILES=	bin/${PORTNAME}

.include <bsd.port.mk>
