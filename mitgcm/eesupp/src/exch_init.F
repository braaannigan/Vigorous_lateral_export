C $Header: /u/gcmpack/MITgcm/eesupp/src/exch_init.F,v 1.6 2004/03/27 03:51:51 edhill Exp $
C $Name:  $

#include "CPP_EEOPTIONS.h"

CBOP
C     !ROUTINE: EXCH_INIT

C     !INTERFACE:
      SUBROUTINE EXCH_INIT
      IMPLICIT NONE

C     !DESCRIPTION:
C     *==========================================================*
C     | SUBROUTINE EXCH\_INIT                                     |
C     | o Initialise WRAPPER exchange data structures.           |
C     *==========================================================*

C     !USES:
C     == Global variables ==
#include "SIZE.h"
#include "EEPARAMS.h"
#include "EESUPPORT.h"
#include "EXCH.h"

C     !LOCAL VARIABLES:
C     == Local variables ==
C     bi, bj - Loop counters
      INTEGER bi, bj
CEOP

      DO bj=1,nSy
       DO bi=1,nSx
        exchangeBufLevel(1,bi,bj)   = 1
        exchRecvXSpinCount(1,bi,bj) = 0
        exchRecvXSpinMax  (1,bi,bj) = 0
        exchRecvXSpinMin  (1,bi,bj) = 1000000000
        exchRecvYSpinCount(1,bi,bj) = 0
        exchRecvYSpinMax  (1,bi,bj) = 0
        exchRecvYSpinMin  (1,bi,bj) = 1000000000
       ENDDO
      ENDDO

      exchCollectStatistics = .TRUE.

      RETURN
      END
