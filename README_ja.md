python-winscard
===============

winscard.dll wrapper using ctypes

## �g�����̗�
*���J�[�h���[�_�[���P��ڑ����Ă���Ɖ���*

import winscard

sc = winscard.SCard()

readers = sc.list_readers() #�J�[�h���[�_�[���������߂̃C���X�^���X�̃��X�g������

r = readers[0] #�P��Ȃ̂�

r.connect()

\# card ID���擾���邽�߂�APDU�R�}���h�𑗐M����B
\# ���ʂ�int(0�`255)�̃��X�g�ŋA���Ă���B

cardid = reader.transmit((0xFF, 0xCA, 0x00, 0x00, 0x00), winscard.SCARD_PCI_T1)

print [hex(x) in cardid]

## ����
* ���ݎd�l�����m��ȕ���������
    * ��{�I�ɂ͂Ȃ�ׂ��������ȃ��C�u�����ɂ������ōl���Ă���B�ᐅ���ȑ��삪�ł���̂͂��łɂ��낢�날�邵�B
* ����������������
    * ���ɁASCardGetStatusChange�ɂ�������̂���������Ă��Ȃ��̂����Bwhile���[�v�œ��̈����|�[�����O�����n���ɂȂ�B

## ����
* �X�}�[�g�J�[�h�V�сH���y�����s�������Ŏ�����i�߂�
* �d�l���ł܂�����PyPI�֓o�^
* ���[�_�[�������䂠����ł̃e�X�g���ł��Ă��Ȃ��̂ł��̂����s��