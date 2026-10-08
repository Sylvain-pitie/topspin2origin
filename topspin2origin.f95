program top2origin
implicit none
integer :: i,j,k,step,leng,trimtext
integer,dimension(:), allocatable :: numat
real*8 :: beginspec, endspec, allppm, ppmstep
real*8, dimension(:), allocatable :: intensite, ppm
real*8, dimension(35,3) :: coordtop, coordbot, coordtopAg, coordbotAg, coordtopPt, coordbotPt
character*128, dimension(:), allocatable :: charatom
character*128,dimension(117):: atomchar
character*128 :: outputorigin, inputtop,elecatm
character*128 :: trash
logical :: stay
!===========================================================================!
!========================lecture fichier txt top spin=======================!
!===========================================================================!
call getarg(1,inputtop)
leng=trimtext(inputtop)
inputtop=trim(inputtop)

outputorigin= inputtop(1:leng-4)//'.CSV'
write(*,*) outputorigin
open(10,file=inputtop,status='old',action='read')
read(10,*) 
read(10,*)
read(10,*)
read(10,*) trash, trash, trash, beginspec, trash, trash, trash, endspec
read(10,*)
read(10,*) trash, trash, trash, step
read(10,*)
read(10,*)
read(10,*)
read(10,*)
allppm = endspec-beginspec
ppmstep = allppm/step
write(*,*) ppmstep

allocate(intensite(step),ppm(step))
ppm(1) = beginspec
do i = 1, step
   read(10,*) intensite(i)
   if (i .ge. 2) then
      ppm(i) = ppm(i-1) + ppmstep
   endif
   if (intensite(i) .lt. 0) then
      intensite(i) = 0
   endif
 !  write(*,*) i, intensite(i), ppm(i)
enddo
 close(10)

165 format(es11.5";"es11.5)
open(10,file=outputorigin, action='write')
do i = 1,step
write(10,165) ppm(i),intensite(i)
enddo
deallocate(intensite)
endprogram
!++++++++++++++++++++++++++++++++++++++++++++Fonctions++++++++++++++++++++++++++++++++++++++++++++++++!
      function trimtext (string)
      implicit none
      integer i,size,last
      integer len,trimtext
      character*1 char
      character*1 null
      character*(*) string
!
!
!     move forward through the string, one character
!     at a time, looking for first null character
!
      trimtext = 0
      size = len(string)
      null = char(0)
      last = size
      do i = 1, size
         if (string(i:i) .eq. null) then
            last = i - 1
            goto 10
         end if
      end do
   10 continue
!
!     move backward through the string, one character
!     at a time, looking for first non-blank character
!
      do i = last, 1, -1
         if (string(i:i) .gt. ' ') then
            trimtext = i
            goto 20
         end if
      end do
   20 continue
      return
      end

