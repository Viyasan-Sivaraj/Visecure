import streamlit as st 


st.title(":blue[Visecure] APP & DNS")

st.markdown("""
<style>
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

h3{
    font-size:20px;
}


.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

.container{
    border : 1px solid;
    border-radius:15px;
    border-radius:15px;
    padding:15px;
    margin :7px;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>

<div class="container" style="display:flex;justify-content:space-between;align-item:center;flex-direction:column;width:100%;font-size:18px;">
    <div style="width:100%;padding:10px;display:flex;justify-content:space-between;">
        <h3>Spam Email Detection</h3>
        <label class="switch">
            <input type="checkbox">
            <span class="slider round"></span>
        </label>
    </div>
    <div style="width:100%;padding:10px;display:flex;justify-content:space-between">
        <h3>Device Security & File Scan</h3>
        <label class="switch">
            <input type="checkbox">
            <span class="slider round"></span>
        </label>
    </div>
    <div style="width:100%;padding:10px;display:flex;justify-content:space-between">
        <h3>Ad Blocker</h3>
        <label class="switch">
            <input type="checkbox">
            <span class="slider round"></span>
        </label>
    </div>
    <div style="width:100%;padding:10px;display:flex;justify-content:space-between;flex-direction:column;">
        <h3>Real Time Verification :</h3>
        <ul>
            <li><div style="width:100%;padding:10px;display:flex;justify-content:space-between">
                <h3>Calls</h3>
                <label class="switch">
                    <input type="checkbox">
                    <span class="slider round"></span>
                </label>
            </div></li>
            <li><div style="width:100%;padding:10px;display:flex;justify-content:space-between">
                <h3>SMS</h3>
                <label class="switch">
                    <input type="checkbox">
                    <span class="slider round"></span>
                </label>
            </div></li>
            <li><div style="width:100%;padding:10px;display:flex;justify-content:space-between">
                <h3>UPI ID</h3>
                <label class="switch">
                    <input type="checkbox">
                    <span class="slider round"></span>
                </label>
            </div></li>
            <li><div style="width:100%;padding:10px;display:flex;justify-content:space-between">
                <h3>Email</h3>
                <label class="switch">
                    <input type="checkbox">
                    <span class="slider round"></span>
                </label>
            </div></li>
        </ul>
    </div>
    <div style="width:100%;padding:10px;display:flex;justify-content:space-between">
        <h3>Threat Detection </h3>
        <label class="switch">
            <input type="checkbox">
            <span class="slider round"></span>
        </label>
    </div>
    <div style="width:100%;padding:10px;display:flex;justify-content:space-between">
        <h3>VPN</h3>
        <label class="switch">
            <input type="checkbox">
            <span class="slider round"></span>
        </label>
    </div>
    <div style="width:100%;padding:10px;display:flex;justify-content:space-between">
        <h3>Obscence Blocker</h3>
        <label class="switch">
            <input type="checkbox">
            <span class="slider round"></span>
        </label>
    </div>
    <div style="width:100%;padding:10px;display:flex;justify-content:space-between">
        <h3>Privacy Mode</h3>
        <label class="switch">
            <input type="checkbox">
            <span class="slider round"></span>
        </label>
    </div>
    <div style="width:100%;padding:10px;display:flex;justify-content:space-between">
        <h3>Secure Camera & Microphone access</h3>
        <label class="switch">
            <input type="checkbox">
            <span class="slider round"></span>
        </label>
    </div>
</div>

""",
unsafe_allow_html=True
)

c31,c11,c12 = st.columns([3,1,5])
c11.image("logo.png", width=200)
