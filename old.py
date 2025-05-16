import subprocess
import getpass
# 터미널용으로 만들어보기!!

def 설정_절전모드(화면꺼짐시간: int, 기본절전시작시간: int, 최대절전시간: int):
    try:
        standbydelay = 최대절전시간 * 60
        displaysleep = 화면꺼짐시간
        sleep = 기본절전시작시간
        # pmset 명령어가 최대절전시간만 초로 받음 나머지는 분으로 받음 왜지???

        # AppleScript로 비밀번호 입력창 띄워서 sudo 권한 받기
        script = '''
        display dialog "절전 설정을 위해 관리자 비밀번호를 입력하세요:" default answer "" with hidden answer buttons {"확인"} default button "확인"
        '''
        result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)

        if result.returncode != 0:
            print("비밀번호 입력 취소됨.")
            return

        # AppleScript 출력에서 비밀번호 추출
        for line in result.stdout.splitlines():
            if line.startswith("text returned:"):
                password = line.split(":", 1)[1].strip()
                break
        else:
            print("비밀번호를 가져오지 못했습니다.")
            return

        # sudo 명령 실행을 위한 전체 pmset 명령어
        pmset_cmd = f'''
        echo "{password}" | sudo -S pmset -a displaysleep {displaysleep} sleep {sleep} hibernatemode 3 standby 1 standbydelaylow {standbydelay} standbydelayhigh {standbydelay}
        '''

        # 실제 명령 실행
        subprocess.run(pmset_cmd, shell=True, check=True)
        print("절전 설정이 성공적으로 적용되었습니다.")

    except subprocess.CalledProcessError as e:
        print("명령 실행 중 오류 발생:", e)
    except Exception as e:
        print("예기치 못한 오류:", e)

# 예시 호출
설정_절전모드(
    화면꺼짐시간=10,
    기본절전시작시간=30,
    최대절전시간=30
)
