import subprocess
# 관리자로 로그인하지 않은 상태에서는 로그인 관련 문제 발생


def 설정_절전모드(화면꺼짐시간: int, 기본절전시작시간: int, 최대절전시간: int):
    try:
        # AppleScript로 사용자에게 안내 메시지 표시
        안내스크립트 = '''
        display dialog "절전 시간 설정을 시작합니다. 모든 시간은 '분 단위'로 입력하세요." buttons {"확인"} default button "확인"
        '''
        subprocess.run(["osascript", "-e", 안내스크립트])

        # AppleScript로 비밀번호 입력받기
        pw_script = '''
        display dialog "절전 설정을 위해 관리자 비밀번호를 입력하세요:" default answer "" with hidden answer buttons {"확인"} default button "확인"
        '''
        result = subprocess.run(["osascript", "-e", pw_script], capture_output=True, text=True)

        if result.returncode != 0:
            print("비밀번호 입력 취소됨.")
            return

        for line in result.stdout.splitlines():
            if line.startswith("text returned:"):
                password = line.split(":", 1)[1].strip()
                break
        else:
            print("비밀번호를 가져오지 못했습니다.")
            return

        # 시간 설정
        standbydelay = 최대절전시간 * 60  # 최대 절전만 초 단위
        # displaysleep, sleep은 분 단위 그대로 사용
        pmset_cmd = f'''
        echo "{password}" | sudo -S pmset -a displaysleep {화면꺼짐시간} sleep {기본절전시작시간} hibernatemode 3 standby 1 standbydelaylow {standbydelay} standbydelayhigh {standbydelay}
        '''

        subprocess.run(pmset_cmd, shell=True, check=True)
        print("✅ 절전 설정이 성공적으로 적용되었습니다.")

    except subprocess.CalledProcessError as e:
        print("❌ 명령 실행 중 오류 발생:", e)
    except Exception as e:
        print("❌ 예기치 못한 오류:", e)


# 예시 실행
설정_절전모드(
    화면꺼짐시간=10,
    기본절전시작시간=30,
    최대절전시간=30
)
