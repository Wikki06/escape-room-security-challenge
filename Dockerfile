FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    findutils \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN mkdir -p /app/challenge /app/data /tmp/escape_room
RUN for i in $(seq 1 500); do echo "log entry $i" > /app/data/log_$i.txt; done
RUN echo "CLUE_COMMAND=system_flag_dump" > /tmp/escape_room/clue.txt
RUN echo "FLAG{c4psul3_3sc4p3_r00m_c0mpl3t3d}" > /app/flag.txt && \
    chmod 600 /app/flag.txt
RUN cat << 'EOF' > /app/challenge/challenge.py
import sys
import os
import subprocess
def read_file(filepath):
    # Bug: basic join lets inputs like "../../tmp/..." escape /app/data
    full_path = os.path.join("/app/data", filepath)
    if os.path.exists(full_path):
        with open(full_path, 'r') as f:
            return f.read().strip()
    return "Error: File not found"
def run_command(clue):
    # Intentionally vulnerable command-injection stage
    cmd = "echo " + clue
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return res.stdout.strip()
if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    action, arg = sys.argv[1], sys.argv[2]
    if action == "--read-file":
        print(read_file(arg))
    elif action == "--exec-clue":
        print(run_command(arg))
EOF
COPY solve.sh /app/solve.sh
COPY eval.py /app/eval.py
RUN chmod +x /app/solve.sh /app/eval.py
ENV PYTHONUNBUFFERED=1
CMD ["/bin/bash"]